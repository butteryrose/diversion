from umeng.dao.model.launch_users_analysis import LaunchUsersAnalysis


def save_and_update(session, users_analysis=[]):
    for user in users_analysis:
        result = session.query(LaunchUsersAnalysis)\
                .filter(LaunchUsersAnalysis.app_id == user.app_id,
                        LaunchUsersAnalysis.channel_id == user.channel_id,
                        LaunchUsersAnalysis.analysis_type == user.analysis_type,
                        LaunchUsersAnalysis.occ_date == user.occ_date).first()
        if result is None:
            session.add(user)
        else:
            user.id = result.id
            session.merge(user)
