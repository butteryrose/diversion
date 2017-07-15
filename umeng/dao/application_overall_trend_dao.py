#!/usr/bin/env python3
# encoding: utf-8
from umeng.dao.model.application_overall_trend import ApplicationOverallTrend


def save_application_overall_trend(session, application_overall_trend=ApplicationOverallTrend()):
        old_overview = session.query(ApplicationOverallTrend).\
            filter(ApplicationOverallTrend.app_id == application_overall_trend.app_id).first()
        if old_overview is None:
            session.add(application_overall_trend)
        else:
            application_overall_trend.id = old_overview.id
            session.merge(application_overall_trend)
