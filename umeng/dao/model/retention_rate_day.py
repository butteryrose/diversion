#!/usr/bin/env python3
# encoding: utf-8
from common.base import base_model
from sqlalchemy import Column, Integer, Date, Float,VARCHAR

class RetentionRateDay(base_model.BaseModel):
    __tablename__ = "t_retention_rate_day"

    id = Column(Integer, primary_key=True, autoincrement=True)
    occ_date = Column(Date)
    app_id = Column(VARCHAR(100))
    install_users = Column(Integer)
    channel_id = Column(VARCHAR(50))
    retention_rate_1 = Column(Float)
    retention_rate_2 = Column(Float)
    retention_rate_3 = Column(Float)
    retention_rate_4 = Column(Float)
    retention_rate_5 = Column(Float)
    retention_rate_6 = Column(Float)
    retention_rate_7 = Column(Float)
    retention_rate_14 = Column(Float)
    retention_rate_30 = Column(Float)
