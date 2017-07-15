#!/usr/bin/env python3
# encoding: utf-8
from umeng.dao.model.application_overview import ApplicationOverview


def save_application_overview(session, application_overviews=[]):
    for application_overview in application_overviews:
        old_overview = session.query(ApplicationOverview).\
            filter(ApplicationOverview.app_id == application_overview.app_id).first()
        if old_overview is None:
            session.add(application_overview)
        else:
            application_overview.id = old_overview.id
            session.merge(application_overview)


def query_all_application_overview(session):
    return session.query(ApplicationOverview).all()
