#!/usr/bin/env python3
# encoding: utf-8
from apscheduler.schedulers.blocking import BlockingScheduler
import common.log.init_logger as log
import common.ex.exception as ex
from umeng.services.user_overview_service import UserOverviewService
from umeng.services.application_overview_service import ApplicationOverviewService
from umeng.services.retention_rate_day_service import RetentionRateDayService
from umeng.services.new_users_analysis_service import NewUsersAnalysisService
from umeng.services.active_users_analysis_service import ActiveUsersAnalysisService
from umeng.services.channel_service import ChannelService
from umeng.services.launch_users_analysis_service import LaunchUsersAnalysisService
from umeng.services.application_overall_trend_service import ApplicationOverallTrendService

def start():
    scheduler = BlockingScheduler()
    try:
        # using in test,run every 10s
        # scheduler.add_job(UserOverviewService().collect_data, trigger="cron", second="*/5")
        # scheduler.add_job(ApplicationOverviewService().collect_data, trigger="cron", second="*/5")
        #
        # scheduler.add_job(UserOverviewService().collect_data, trigger="cron", hour="*/1")
        # scheduler.add_job(ApplicationOverviewService().collect_data, trigger="cron", hour="*/1")
        # scheduler.add_job(ApplicationOverallTrendService().collect_data, trigger="cron", hour="*/1")
        # scheduler.add_job(RetentionRateDayService().collect_data, trigger="cron", day="*/1", hour="1")
        # scheduler.add_job(NewUsersAnalysisService().collect_data, trigger="cron", day="*/1", hour="1")
        # scheduler.add_job(ActiveUsersAnalysisService().collect_data, trigger="cron", day="*/1", hour="1")
        # scheduler.add_job(LaunchUsersAnalysisService().collect_data, trigger="cron", day="*/1", hour="1")
        # scheduler.add_job(ChannelService().collect_data, trigger="cron", day="*/1", hour="1")
        # UserOverviewService().collect_data()
        # ApplicationOverviewService().collect_data()
        ApplicationOverallTrendService().collect_data()
        # ChannelService().collect_data()
        # RetentionRateDayService().collect_data()
        # NewUsersAnalysisService().collect_data()
        # ActiveUsersAnalysisService().collect_data()
        # LaunchUsersAnalysisService().collect_data()
        # scheduler.add_job(LaunchUsersAnalysisService().collect_data, trigger="cron", second="*/100")
        # scheduler.start()
    except Exception as e:
        log.get_log().error("启动采集任务")
        ex.collection_ex(e)

# if __name__ == '__main__':
#     start()
