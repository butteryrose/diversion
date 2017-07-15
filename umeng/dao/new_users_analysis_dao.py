from umeng.dao.model.new_users_analysis import NewUsersAnalysis


def save_and_update(session, new_users_analysis=[]):
    for new_user in new_users_analysis:
        result = session.query(NewUsersAnalysis).filter(NewUsersAnalysis.app_id == new_user.app_id,
                                                        NewUsersAnalysis.channel_id == new_user.channel_id,
                                                        NewUsersAnalysis.analysis_type == new_user.analysis_type,
                                                        NewUsersAnalysis.occ_date == new_user.occ_date).first()
        if result is None:
            session.add(new_user)
        else:
            new_user.id = result.id
            session.merge(new_user)
