#!/usr/bin/env python3
# encoding: utf-8

from common.base import base_model
from sqlalchemy import Column, Integer, VARCHAR, DateTime
from common.utils import date_utils


class UserOverview(base_model.BaseModel):
    __tablename__ = "t_user_overview"

    id = Column(Integer, primary_key=True, autoincrement=True)
    installs_today = Column(Integer)
    active_users_today = Column(Integer)
    launches_today = Column(Integer)
    total_installs = Column(Integer)
    installs_yesterday = Column(Integer)
    active_users_yesterday = Column(Integer)
    launches_yesterday = Column(Integer)
    total_installs_yesterday = Column(Integer)
    uniq_active_users_yesterday = Column(Integer)
    uniq_installs_yesterday = Column(Integer)
    update_time = Column(DateTime, default=date_utils.get_date())
