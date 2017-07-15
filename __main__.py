#!/usr/bin/env python3
# encoding: utf-8
from cache import config
from common.base import dao_manager
from umeng.dao.model.retention_rate_day import RetentionRateDay
from umeng import task_manager


def __init_config():
    """"
        load yml file and cache config data
    """
    config.load_config()

if __name__ == '__main__':
    __init_config()
    dao_manager.init()
    dao_manager.create_table()
    task_manager.start()
    # print(time.time())
   #  # driverPath = '/Users/xuebj/Documents/phantomjs-2.1.1-macosx/bin/phantomjs'
   #  # webdriver
   #  driver = webdriver.Chrome(executable_path="./driver/chromedriver")
   # #  # url =  "http://www.baidu.com"
   # #  # driver.get(url)
   # #  # wait = WebDriverWait(driver,30)
   # #  # for co
   #  url = 'https://i.umeng.com/login'
   #  driver.get(url)
   #  wait = WebDriverWait(driver,30)
   #  driver.find_element_by_css_selector("#ump .loginForm .list input[type='text']").send_keys("hsmaidanbao@163.com")
   #  driver.find_element_by_css_selector("#ump .loginForm .list input[type='password']").send_keys("hstzyj2016")
   #  driver.find_element_by_id('submitForm').click()
   #  s = requests.Session()
   #  for cookie in driver.get_cookies():
   #      c = requests.cookies.RequestsCookieJar()
   #      c.set(cookie['name'], cookie['value'],path=cookie['path'],domain=cookie['domain'])
   #      s.cookies.update(c)
   #  r = s.get("http://mobile.umeng.com/apps/get_summary_data")
   #  print(r.json())
   # #  driver.quit()
   #  from common.utils import json_util
   #  __init_config()
   #  base_dao.init()
   #  base_dao.create_table()
   #  user_overview = UserOverview()
   #  json_obj = {"total_installs":"4984560","installs_today":"66","active_users_today":"1972","launches_today":"7178","installs_yesterday":"90","active_users_yesterday":"1577","launches_yesterday":"4663","total_installs_yesterday":"4984494","uniq_installs_yesterday":"90","uniq_active_users_yesterday":"1577"}
   #  json_util.json_to_object(user_overview, json_obj)
   #  # user_overview = UserOverview(total_installs=254094,installs_today=2061,active_users_today=2557,
   #  #                                    launches_today=16332,installs_yesterday=320,active_users_yesterday=3279,
   #  #                                    launches_yesterday=20916,total_installs_yesterday=253888,
   #  #                                    uniq_installs_yesterday=320,uniq_active_users_yesterday=3279)
   #  base_dao.execute(user_overview_dao.save_user_overview, user_overview=user_overview)
