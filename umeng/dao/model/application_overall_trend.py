from common.base import base_model
from sqlalchemy import Column, Integer, VARCHAR, DateTime, Float,Numeric
from common.utils import date_utils


class ApplicationOverallTrend(base_model.BaseModel):

    __tablename__ = "t_application_overall_trend"

    id = Column(Integer, primary_key=True, autoincrement=True)
    app_id = Column(VARCHAR(100))
    errors = Column(VARCHAR(100))
    install = Column(Integer)
    last7day_active_user_amount = Column(Integer)
    last7day_active_user_growth = Column(VARCHAR(100))
    last7day_daily_duration_amount = Column(VARCHAR(100))
    last7day_daily_duration_growth = Column(VARCHAR(100))
    last30day_active_user_amount = Column(Integer)
    last30day_active_user_growth = Column(VARCHAR(100))
    update_date = Column(DateTime, default=date_utils.get_date())

