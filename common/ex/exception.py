import common.log.init_logger as log
import sys
import traceback


def collection_ex(e):
    ty, tv, tb = sys.exc_info()
    log.get_log().critical("异常对象：%s" % e)
    log.get_log().critical("错误类型：{0},错误详细信息：{1}".format(ty, tv))
    log.get_log().critical("".join(traceback.format_tb(tb)))