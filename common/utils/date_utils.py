#!/usr/bin/env python3
# encoding: utf-8
import time
import datetime
import re

date_re = re.compile(r"^20\d{2}-\d{2}-\d{2}$")
datetime_minute_re = re.compile(r"^20\d{2}-\d{2}-\d{2} \d{2}:\d{2}$")
datetime_second_re = re.compile(r"^20\d{2}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$")


def get_format_date_time(pattern="%Y-%m-%d %H:%M:%S"):
    return time.strftime(pattern, time.localtime())


def get_format_date(pattern="%Y-%m-%d"):
    return time.strftime(pattern, time.localtime())


def get_before_n_days(date_str, n):
    return str_to_date(date_str) + datetime.timedelta(days=n)


def str_to_date(date_str):
    pattern = "%Y-%m-%d"
    if date_re.match(date_str):
        pattern = "%Y-%m-%d"
    elif datetime_minute_re.match(date_str):
        pattern = "%Y-%m-%d %H:%M"
    elif datetime_second_re.match(date_str):
        pattern = "%Y-%m-%d %H:%M:%S"
    return datetime.datetime.strptime(date_str, pattern)


def get_year_month_day(date_str):
    return date_str[0:10]


def get_before_n_day(n):
    return get_date() + datetime.timedelta(days=n)


def get_date():
    return datetime.datetime.now()

if __name__ == '__main__':
    print(get_year_month_day("2015-09-01 12:1"))
