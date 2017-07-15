#!/usr/bin/env python3
# encoding: utf-8
import common.file.io as io


config_data = {}


def load_config():
    config_data.update(io.load_yml("application.yml"))


def get_global():
    return config_data["diversion"]["global"]


def get_umeng():
    return config_data["diversion"]["umeng"]
