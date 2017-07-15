from cache import config
from umeng.services import base_service
from umeng.dao import collect_position_dao
from umeng.dao import channle_dao
from common.utils import date_utils
from umeng.dao.model.channel import Channel


class UserAnalysisService(base_service.BaseService):
    statistics_period = ["hourly", "daily", "weekly", "monthly"]

    def __init__(self, name="用户分析"):
        self.name = name
        self.url = config.get_umeng()["url"]["user_analysis"]

    def collect_data(self):
        apps = self.get_apps()
        old_name = self.name
        for app in apps:
            for period in self.get_statistics_period():
                if period == "hourly":  # hourly analysis 不区分 channel
                    self.name = old_name + "[小时统计不分渠道]"
                    self.set_hourly_url()
                    self.__collect_by_app(app=app, channel=Channel(channel_id=b"", name=b"hour data"), period=period)
                    self.name = old_name
                else:
                    self.set_other_url()
                    channels = self.execute(function=lambda session, app_id:
                                            channle_dao.query_channel(session=session, app_id=app_id),
                                            app_id=app.app_id.decode())
                    for channel in channels:
                        self.name = old_name + channel.name.decode() + "[" + channel.channel_id.decode() + "]"
                        self.__collect_by_app(app=app, channel=channel, period=period)
                        self.name = old_name

    def __collect_by_app(self, app, channel, period):
        self.collect_data_inner(url=self.url.format(app_id=app.app_id.decode(),
                                                    start_date=self.__get_pre_collect_date(
                                                        app_id=app.app_id.decode(),
                                                        period=period,
                                                        channel_id=channel.channel_id.decode()),
                                                    end_date=date_utils.get_format_date(),
                                                    time_unit=period,
                                                    stats=self.get_stats(),
                                                    channel_id=channel.channel_id.decode()),
                                name=self.name + "--" + app.name.decode() + "渠道:" + channel.name.decode() + "[" + period + "]",
                                app_id=app.app_id.decode(),
                                period=period,
                                channel_id=channel.channel_id.decode())

    def callback(self, result, **kwargs):
        self.transaction_execute(function=self.save_and_update,
                                 result=result,
                                 app_id=kwargs["app_id"],
                                 period=kwargs["period"],
                                 channel_id=kwargs["channel_id"])

    def __get_pre_collect_date(self, app_id="", period="", channel_id=""):
        return self.execute(function=lambda session, subject, default_value:
                            collect_position_dao.get_by_subject(session=session,
                                                                subject=subject,
                                                                default_value=default_value),
                            subject=self.get_subject_name(app_id, period, channel_id),
                            default_value=str(config.get_global()["history_start_date"]))

    def get_subject_name(self, app_id="", period="", channel_id=""):
        return self.get_subject() + "_" + app_id + "_" + channel_id + "_" + period

    def save_and_update(self, session, result, app_id, period, channel_id):
        pass

    def get_subject(self):
        pass

    def get_stats(self):
        pass

    def get_statistics_period(self):
        return self.statistics_period

    def set_hourly_url(self):
        self.url = config.get_umeng()["url"]["user_analysis"]

    def set_other_url(self):
        self.url = config.get_umeng()["url"]["user_analysis"]
