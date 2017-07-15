#!/usr/bin/env python3
# encoding: utf-8
from cache import config
from umeng.dao.model.user_overview import UserOverview
from common.utils import json_util
from common.utils import date_utils
from umeng.dao import user_overview_dao
from common.base import base_dao
from umeng.services.base_service import BaseService


class UserOverviewService(BaseService):

    def __init__(self, name="全局概要信息采集任务"):
        self.name = name
        self.url = config.config_data["diversion"]["umeng"]["url"]["user_overview"]

    def callback(self, result):
        for key in result.keys():
            result[key] = int(result[key])
            user_overview = UserOverview()
            user_overview.update_time = date_utils.get_date()
            json_util.json_to_object(user_overview, result)
            self.transaction_execute(function= lambda session, user_overview:
                                     user_overview_dao.save_user_overview(session=session, user_overview=user_overview),
                                     user_overview=user_overview)
