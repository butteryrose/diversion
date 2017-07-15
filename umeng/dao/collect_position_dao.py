from umeng.dao.model.collect_position import CollectPosition
from common.utils import date_utils


def get_by_subject(session,subject="", default_value=""):
    result = session.query(CollectPosition).filter(CollectPosition.subject == subject).first()
    if result is None:
        return default_value
    else:
        return result.position.decode()


def update_by_subject(session,subject="", value=""):
    collect_position = CollectPosition(subject=subject, position=value, date_time=date_utils.get_date())
    result = session.query(CollectPosition).filter(CollectPosition.subject == subject).first()
    if result is None:
        session.add(collect_position)
    else:
        collect_position.id = result.id
        session.merge(collect_position)
