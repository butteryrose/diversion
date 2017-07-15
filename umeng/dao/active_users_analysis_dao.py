from umeng.dao.model.active_users_analysis import ActiveUsersAnalysis


def save_and_update(session, users_analysis=[]):
    for user in users_analysis:
        result = session.query(ActiveUsersAnalysis)\
            .filter(ActiveUsersAnalysis.app_id == user.app_id,
                    ActiveUsersAnalysis.channel_id == user.channel_id,
                    ActiveUsersAnalysis.analysis_type == user.analysis_type,
                    ActiveUsersAnalysis.occ_date == user.occ_date).first()
        if result is None:
            session.add(user)
        else:
            user.id = result.id
            session.merge(user)
