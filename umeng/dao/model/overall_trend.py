#!/usr/bin/env python3
# encoding: utf-8
from common.base import base_model
from sqlalchemy import Column, Integer, VARCHAR
from common.utils import date_utils

class OverallTrend(base_model.BaseModel):
    __tablename__ = "t_overall_trend"

    id = Column(Integer, primary_key=True, autoincrement=True)
    trend_new_users = Column(Integer)   #新增用户
    trend_active_users = Column(Integer)  #活跃用户
    trend_launches = Column(Integer)  #启动次数
    trend_installations = Column(Integer)  #累计用户
    trend_active_new_users = Column(Integer)  #活跃新用户
    trend_active_old_users = Column(Integer)  #活跃老用户
    trend_new_users_rate = Column(Integer)  #活跃用户中新用户占比
    trend_morrow_retention = Column(Integer)  #次日留存率
    trend_avg_duration = Column(Integer)  #平均单次使用时长
    trend_daily_avg_launches = Column(Integer)  #平均日启动次数
