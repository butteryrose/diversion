from common.base import base_model
from sqlalchemy import Column, Integer, VARCHAR, DateTime


class NewUsersAnalysis(base_model.BaseModel):
    __tablename__ = "t_new_users_analysis"

    id = Column(Integer, primary_key=True, autoincrement=True)
    occ_date = Column(DateTime)
    app_id = Column(VARCHAR(100))
    new_users = Column(Integer)
    channel_id = Column(VARCHAR(50))
    analysis_type = Column(VARCHAR(10))  # hourly weekly daily monthly
