from common.base import base_model
from sqlalchemy import Column, Integer, VARCHAR, Date
from common.utils import date_utils


class ActiveUsersAnalysis(base_model.BaseModel):
    __tablename__ = "t_active_users_analysis"

    id = Column(Integer, primary_key=True, autoincrement=True)
    occ_date = Column(Date)
    app_id = Column(VARCHAR(100))
    active_users = Column(Integer)
    channel_id = Column(VARCHAR(50))
    analysis_type = Column(VARCHAR(10))  # weekly daily monthly
