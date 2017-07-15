#!/usr/bin/env python3
# encoding: utf-8
from cache import config
from umeng.dao.model.application_overview import ApplicationOverview
from common.utils import json_util, date_utils
from umeng.dao import application_overview_dao
from umeng.services.base_service import BaseService


class ApplicationOverviewService(BaseService):

    def __init__(self, name="各个app概要数据统计任务"):
        self.name = name
        self.url = config.config_data["diversion"]["umeng"]["url"]["application_user_overview"]

    def callback(self, result):
        application_overviews = []
        for res in result["stats"]:
            if res["name"].find("投资赢家") != -1:
                application_overview = ApplicationOverview()
                json_util.json_to_object(application_overview, res)
                application_overview.update_date = date_utils.get_date()
                application_overviews.append(application_overview)
        self.transaction_execute(
            function=lambda session, application_overviews:
            application_overview_dao.save_application_overview(session=session,
                                                               application_overviews=application_overviews),
            application_overviews=application_overviews
        )
