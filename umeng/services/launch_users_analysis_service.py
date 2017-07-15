from umeng.services import user_analysis_service
from umeng.dao.model.launch_users_analysis import LaunchUsersAnalysis
from common.utils import date_utils
from umeng.dao import launch_users_analysis_dao, collect_position_dao
from cache import config


class LaunchUsersAnalysisService(user_analysis_service.UserAnalysisService):

    def __init__(self, name="启动次数分析"):
        user_analysis_service.UserAnalysisService.__init__(self, name)

    def save_and_update(self, session, result, app_id, period, channel_id):
        if period == "hourly":
            self.save_and_update_hourly(session, result, app_id, period, channel_id)
        else:
            self.save_and_update_other(session, result, app_id, period, channel_id)

    def save_and_update_hourly(self, session, result, app_id, period, channel_id):
            datas = result["stats"]
            users = []
            for i in range(0, len(datas)):
                users.append(LaunchUsersAnalysis(occ_date=date_utils.str_to_date(datas[i]["date"]),
                                                 launch_users=datas[i]["data"],
                                                 analysis_type=period,
                                                 app_id=app_id,
                                                 channel_id=channel_id))
            launch_users_analysis_dao.save_and_update(session=session, users_analysis=users)
            collect_position_dao.update_by_subject(session=session,
                                                   subject=self.get_subject_name(app_id, period, channel_id),
                                                   value=date_utils.get_year_month_day(datas[0]["date"]))

    def save_and_update_other(self, session, result, app_id, period, channel_id):
        dates = result["dates"]
        data = result["stats"][0]["data"]
        users = []
        for i in range(0, len(dates)):
            users.append(LaunchUsersAnalysis(occ_date=date_utils.str_to_date(dates[i]),
                                             launch_users=data[i],
                                             analysis_type=period,
                                             app_id=app_id,
                                             channel_id=channel_id))
        launch_users_analysis_dao.save_and_update(session=session, users_analysis=users)
        collect_position_dao.update_by_subject(session=session,
                                               subject=self.get_subject_name(app_id, period, channel_id),
                                               value=date_utils.get_year_month_day(dates[-1]))

    def get_subject(self):
        return "user_analysis_launch"

    def get_stats(self):
        return "launches"

    def set_hourly_url(self):
        self.url = config.get_umeng()["url"]["user_analysis_launch_hourly"]
