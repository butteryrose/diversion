#!/usr/bin/env python3
# encoding: utf-8
import json


def json_to_object(class_obj, json_o):
    if isinstance(json_o, str):
        _json_object = json.loads(json_o)
    elif isinstance(json_o, dict):
        _json_object = json_o
    for key in _json_object.keys():
        if hasattr(class_obj, key):
            class_obj.__dict__[key] = _json_object[key]


if __name__ == '__main__':
    from umeng.dao.model.user_overview import UserOverview
    user_overview = UserOverview()
    json_object = {"total_installs":"4984560","installs_today":"66","active_users_today":"1972","launches_today":"7178","installs_yesterday":"90","active_users_yesterday":"1577","launches_yesterday":"4663","total_installs_yesterday":"4984494","uniq_installs_yesterday":"90","uniq_active_users_yesterday":"1577"}
    json_to_object(user_overview, json_object)
    print(user_overview.active_users_today)
