#!/usr/bin/env python3
# encoding: utf-8
from cache import config
from umeng.dao.model.application_overall_trend import ApplicationOverallTrend
from common.utils import json_util, date_utils
from umeng.dao import application_overall_trend_dao
from umeng.services.base_service import BaseService


class ApplicationOverallTrendService(BaseService):

    def __init__(self, name="各个app整体趋势数据统计任务"):
        self.name = name
        self.url = config.config_data["diversion"]["umeng"]["url"]["application_overall_trend"]

    def collect_data(self):
        apps = self.get_apps()
        old_name = self.name
        for app in apps:
            self.__collect_by_app(app=app)
            self.name = old_name

    def __collect_by_app(self, app):
        self.collect_data_inner(url=self.url.format(app_id=app.app_id.decode()),
                                name=self.name + "--" + app.name.decode(),
                                app_id=app.app_id.decode())

    def callback(self, result, **keywords):
        data = result["stats"]
        if data is not None:
            application_overall_trend = \
                ApplicationOverallTrend(app_id=keywords["app_id"],
                                        errors=str(data["errors"]["amount"]),
                                        install=data["install"]["amount"],
                                        last7day_active_user_amount=data["last7day_active_user"]["amount"],
                                        last7day_active_user_growth=data["last7day_active_user"]["growth"],
                                        last7day_daily_duration_amount=data["last7day_daily_duration"]["amount"],
                                        last7day_daily_duration_growth=data["last7day_daily_duration"]["growth"],
                                        last30day_active_user_amount=data["last30day_active_user"]["amount"],
                                        last30day_active_user_growth=data["last30day_active_user"]["growth"],
                                        update_date=date_utils.get_date())
        self.transaction_execute(
            function=lambda session, application_overall_trend:
            application_overall_trend_dao.save_application_overall_trend(session=session,
                                                               application_overall_trend=application_overall_trend),
            application_overall_trend=application_overall_trend
        )
