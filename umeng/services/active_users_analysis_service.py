from umeng.services import user_analysis_service
from umeng.dao.model.active_users_analysis import ActiveUsersAnalysis
from common.utils import date_utils
from umeng.dao import collect_position_dao, active_users_analysis_dao
from common.log import init_logger as log


class ActiveUsersAnalysisService(user_analysis_service.UserAnalysisService):

    def __init__(self, name="活跃用户分析"):
        user_analysis_service.UserAnalysisService.__init__(self, name)

    def save_and_update(self, session, result, app_id, period, channel_id):
        dates = result["dates"]
        data = result["stats"][0]["data"]
        users = []
        for i in range(0, len(dates)):
            users.append(ActiveUsersAnalysis(occ_date=date_utils.str_to_date(dates[i]),
                                             active_users=data[i],
                                             analysis_type=period,
                                             app_id=app_id,
                                             channel_id=channel_id))
        if len(users) > 0:
            active_users_analysis_dao.save_and_update(session=session, users_analysis=users)

            collect_position_dao.update_by_subject(session=session,
                                                   subject=self.get_subject_name(app_id, period, channel_id),
                                                   value=date_utils.get_year_month_day(dates[-1]))

    def get_subject(self):
        return "user_analysis_active"

    def get_stats(self):
        return "active_users"

    def get_statistics_period(self):
        return self.statistics_period[1:]
