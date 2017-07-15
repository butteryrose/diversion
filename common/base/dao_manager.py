#!/usr/bin/env python3
# encoding: utf-8
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from cache import config
from common.base import base_model


engine = None
Session = None


def init():
    data_sources = config.config_data["diversion"]["data_source"]
    global engine
    engine = create_engine(data_sources["url"],
                           pool_size=data_sources["pool_size"],
                           pool_recycle=data_sources["pool_recycle"],
                           max_overflow=data_sources["max_overflow"],
                           pool_timeout=data_sources["pool_timeout"],
                           echo=data_sources["echo"])
    global Session
    Session = sessionmaker(bind=engine)


def create_table():
    base_model.BaseModel.metadata.create_all(engine)



