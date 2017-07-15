#!/usr/bin/env python3
# encoding: utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests
from cache import config
import common.log.init_logger as log
import common.ex.exception as ex
import time
import threading


request_session_cache = {
    "update_time": time.time(),
    "session": None
}

condition = threading.Condition()


def get_request_session():
    global condition
    condition.acquire()
    if __session_need_update():
        __build_request_session()
    condition.notify()
    condition.release()
    return __get_session()


def __session_need_update():
    return __session_is_none() or __session_is_timeout()


def __session_is_none():
    return request_session_cache["session"] is None


def __session_is_timeout():
    return time.time() > request_session_cache["update_time"] \
                         + config.get_umeng()["session_timeout"]


def __build_request_session():
    driver = __login_umeng()
    s = requests.Session()
    for cookie in driver.get_cookies():
        c = requests.cookies.RequestsCookieJar()
        c.set(cookie['name'], cookie['value'], path=cookie['path'], domain=cookie['domain'])
        s.cookies.update(c)
    __cache_session(s)
    return s


def __login_umeng():
    driver = webdriver.PhantomJS(executable_path=config.get_global()["selenium"]["driver_path"])
    driver.get(config.get_umeng()["url"]["login"])
    wait = WebDriverWait(driver, 30)
    try:
        wait.until(EC.element_to_be_clickable((By.ID, 'submitForm')))
        log.get_log().info("页面加载完成")
    except Exception as e:
        log.get_log().error("等待登录页面错误错误")
        ex.collection_ex(e)
    else:  # auto login
        driver.find_element_by_css_selector("#ump .loginForm .list input[type='text']")\
            .send_keys(config.get_umeng()["user_name"])
        driver.find_element_by_css_selector("#ump .loginForm .list input[type='password']")\
            .send_keys(config.get_umeng()["password"])
        driver.find_element_by_id('submitForm').click()
        time.sleep(5)  # 等待一段时间，用于页面跳转
    return driver


def __cache_session(session):
    request_session_cache["session"] = session


def __get_session():
    request_session_cache["update_time"] = time.time()
    return request_session_cache["session"]


