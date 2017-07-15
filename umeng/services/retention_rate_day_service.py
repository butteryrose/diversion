#!/usr/bin/env python3
# encoding: utf-8
from umeng.services.base_service import BaseService
from cache import config
from umeng.dao import collect_position_dao
from common.utils import date_utils, json_util
from common.log import init_logger as log
from umeng.dao import retention_rate_day_dao
from umeng.dao import channle_dao
from umeng.dao.model.retention_rate_day import RetentionRateDay


class RetentionRateDayService(BaseService):

    """
        留存率 只采集日的，并且部分版本号，区分渠道
    """

    def __init__(self, name="留存率采集任务"):
        """

        :type name: object task name
        """
        self.name = name
        self.url = config.get_umeng()["url"]["retention_rate_day"]

    def collect_data(self):
        apps = self.get_apps()
        for app in apps:
            channels = self.execute(function=lambda session, app_id:
                                    channle_dao.query_channel(session=session, app_id=app_id),
                                    app_id=app.app_id.decode())
            old_name = self.name
            for channel in channels:
                self.name = old_name + channel.name.decode() + "[" + channel.channel_id.decode() + "]"
                _pre_collect_date = self.__get_pre_collect_date(app_id=app.app_id.decode(),
                                                                channel_id=channel.channel_id.decode())
                if _pre_collect_date != date_utils.get_before_n_day(-2).strftime("%Y-%m-%d"):
                    self.collect_data_inner(url=self.url.format(app_id=app.app_id.decode(),
                                                                start_date=self.__get_start_date(_pre_collect_date),
                                                                end_date=date_utils.get_format_date(),
                                                                channel_id=channel.channel_id.decode()),
                                            name=self.name + "--" + app.name.decode(),
                                            app_id=app.app_id.decode(),
                                            channel_id=channel.channel_id.decode())
                else:
                    log.get_log().info(app.name.decode() + "[" + channel.channel_id.decode() + "]" + "采集已经完成,无需重复采集")
            self.name = old_name

    def callback(self, result, **kwargs):
        app_id = kwargs["app_id"]
        datas = []
        if "stats" in result:
            for one in result["stats"]:
                retention_rate = RetentionRateDay()
                json_util.json_to_object(retention_rate,
                                         self.__build_retention_rate_json_str(one, app_id, kwargs["channel_id"]))
                datas.append(retention_rate)
            # 保存数据 和 更新采集记录
            self.transaction_execute(function=self.save_data,
                                     retention_rates=datas,
                                     app_id=app_id,
                                     channel_id=kwargs["channel_id"])

    def save_data(self, session, retention_rates, app_id="", channel_id=""):
        if len(retention_rates) > 0:
            retention_rate_day_dao.save_retention_rate_day(session, retention_rates=retention_rates)
            collect_position_dao.update_by_subject(session,
                                                   subject=self.__get_subject_name(app_id,channel_id),
                                                   value=retention_rates[-1].occ_date.strftime("%Y-%m-%d"))

    @staticmethod
    def __build_retention_rate_json_str(retention_rate, app_id, channel_id):
        json = {
            "app_id": app_id,
            "occ_date": date_utils.get_before_n_days(retention_rate["install_period"], 0),
            "install_users": retention_rate["total_install"],
            "channel_id": channel_id
        }
        rate = retention_rate["retention_rate"]
        for i in range(0, len(rate)):
            if i == 7:
                json["retention_rate_14"] = rate[i]
            elif i == 8:
                json["retention_rate_30"] = rate[i]
            else:
                json["retention_rate_" + str(i+1)] = rate[i]
        return json


    @staticmethod
    def __get_start_date(pre_collect_date=""):
        return date_utils.get_before_n_days(pre_collect_date, -29).strftime("%Y-%m-%d")

    def __get_pre_collect_date(self, app_id="", channel_id=""):
        return self.execute(function=lambda session, subject, default_value:
                            collect_position_dao.get_by_subject(session=session,
                                                                subject=subject,
                                                                default_value=default_value),
                            subject=self.__get_subject_name(app_id,channel_id),
                            default_value=str(config.get_global()["history_start_date"]))

    @staticmethod
    def __get_subject_name(app_id, channel_id):
        return "retention_rate_day_" + app_id + "_" + channel_id
