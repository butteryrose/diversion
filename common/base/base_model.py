#!/usr/bin/env python3
# encoding: utf-8
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

BaseModel = declarative_base()
engine = None
Session = None


def init():
    global engine
    engine = create_engine('sqlite:///:memory:')
    global Session
    Session = sessionmaker(bind=engine)
