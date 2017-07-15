#!/usr/bin/env python3
# encoding: utf-8

from common.base import base_model
from common.utils import date_utils
from sqlalchemy import Column, Integer, VARCHAR, DateTime


class ApplicationOverview(base_model.BaseModel):
    __tablename__ = "t_application_overview"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(100))
    sdk_version = Column(VARCHAR(30))
    app_id = Column(VARCHAR(100))
    platform = Column(VARCHAR(100))
    install_today = Column(Integer)
    install_yesterday = Column(Integer)
    active_today = Column(Integer)
    active_yesterday = Column(Integer)
    launch_today = Column(Integer)
    launch_yesterday = Column(Integer)
    install_all = Column(Integer)
    update_date = Column(DateTime, default=date_utils.get_date())


