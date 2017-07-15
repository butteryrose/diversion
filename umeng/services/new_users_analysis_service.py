from umeng.services import user_analysis_service
from umeng.dao.model.new_users_analysis import NewUsersAnalysis
from common.utils import date_utils
from umeng.dao import collect_position_dao, new_users_analysis_dao


class NewUsersAnalysisService(user_analysis_service.UserAnalysisService):

    def __init__(self, name="新增用户分析"):
        user_analysis_service.UserAnalysisService.__init__(self, name)

    def save_and_update(self, session, result, app_id, period, channel_id):
        if "dates" in result:
            dates = result["dates"]
            data = result["stats"][0]["data"]
            new_users = []
            for i in range(0, len(dates)):
                new_users.append(NewUsersAnalysis(occ_date=date_utils.str_to_date(dates[i]),
                                                  new_users=data[i],
                                                  analysis_type=period,
                                                  app_id=app_id,
                                                  channel_id=channel_id))
            new_users_analysis_dao.save_and_update(session=session, new_users_analysis=new_users)

            collect_position_dao.update_by_subject(session=session,
                                                   subject=self.get_subject_name(app_id, period, channel_id),
                                                   value=date_utils.get_year_month_day(dates[-1]))

    def get_subject(self):
        return "user_analysis_new"

    def get_stats(self):
        return "installations"

