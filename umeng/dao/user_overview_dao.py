#!/usr/bin/env python3
# encoding: utf-8
from umeng.dao.model.user_overview import UserOverview


def save_user_overview(session, user_overview):
    count = session.query(UserOverview).count()
    if count == 0:
        session.add(user_overview)
    else:
        user = session.query(UserOverview).one()
        user_overview.id = user.id
        session.merge(user_overview)
