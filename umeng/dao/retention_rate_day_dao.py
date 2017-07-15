#!/usr/bin/env python3
# encoding: utf-8
from umeng.dao.model.retention_rate_day import RetentionRateDay


def save_retention_rate_day(session, retention_rates=[]):
    for retention_rate in retention_rates:
        result = session.query(RetentionRateDay)\
            .filter(RetentionRateDay.app_id == retention_rate.app_id,
                    RetentionRateDay.occ_date == retention_rate.occ_date,
                    RetentionRateDay.channel_id == retention_rate.channel_id).first()
        if result is None:
            session.add(retention_rate)
        else:
            retention_rate.id = result.id
            session.merge(retention_rate)
