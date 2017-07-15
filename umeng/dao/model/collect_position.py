#!/usr/bin/env python3
# encoding: utf-8


from common.base import base_model
from sqlalchemy import Column, Integer, VARCHAR, DateTime
from common.utils import date_utils


class CollectPosition(base_model.BaseModel):
    __tablename__ = "t_collect_position"

    id = Column(Integer, primary_key=True, autoincrement=True)
    subject = Column(VARCHAR(200))
    position = Column(VARCHAR(100))
    date_time = Column(DateTime, default=date_utils.get_date())
