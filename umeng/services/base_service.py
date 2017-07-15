#!/usr/bin/env python3
# encoding: utf-8
import common.log.init_logger as log
import common.ex.exception as ex
from umeng.session import session_manager
from umeng.dao import application_overview_dao
from common.base import dao_manager


class BaseService(object):

    def collect_data(self):
        self.collect_data_inner(self.url, self.name)

    def collect_data_inner(self, url, name, **kwargs):
        log.get_log().info(name + "开始")
        session = session_manager.get_request_session()
        try:
            r = session.get(url, timeout=10000)
        except Exception as e:
            log.get_log().error(name + "失败")
            ex.collection_ex(e)
        else:
            if r.status_code == 200:
                result = r.json()
                if "ret" not in result or ("result" in result and result["result"] == "success"):
                    if len(kwargs) > 0:
                        self.callback(result, **kwargs)
                    else:
                        self.callback(result)
                else:
                    log.get_log().error("本次[" + name + "]失败[" + result["msg"] + "]")
            log.get_log().info(name + "完成")

    def callback(self, result):
        pass

    def transaction_execute(self, function, **kwargs):
        session = dao_manager.Session()
        try:
            function(session, **kwargs)
        except Exception as e:
            log.get_log().error("执行SQL[" + function.__name__ + "]错误")
            session.rollback()
            ex.collection_ex(e)
        else:
            session.commit()
        finally:
            session.close()

    def execute(self, function, **kwargs):
        session = dao_manager.Session()
        try:
            return function(session, **kwargs)
        except Exception as e:
            log.get_log().error("执行SQL[" + function.__name__ + "]错误")
            ex.collection_ex(e)
        finally:
            session.close()

    def get_apps(self):
        return self.execute(function=lambda session:
                            application_overview_dao.query_all_application_overview(session=session))
