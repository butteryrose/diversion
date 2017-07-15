from common.base import base_model
from sqlalchemy import Column, VARCHAR, Integer


class Channel(base_model.BaseModel):
    __tablename__ = "t_channel"

    id = Column(Integer,primary_key=True, autoincrement=True)
    name = Column(VARCHAR(50))
    channel_id = Column(VARCHAR(50))
    app_id = Column(VARCHAR(50))
    is_shown = Column(VARCHAR(5))
