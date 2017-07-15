#!/usr/bin/env python3
# encoding: utf-8
from common.base import dao_manager
import common.log.init_logger as log
import common.ex.exception as ex


def execute(function, **kwargs):
    session = dao_manager.Session()
    try:
        function(session, **kwargs)
    except Exception as e:
        session.rollback()
        log.get_log().error("执行SQL[" + function.__name__ + "]错误")
        ex.collection_ex(e)
    else:
        session.commit()
    finally:
        session.close()


def get_session():
    return dao_manager.Session()

