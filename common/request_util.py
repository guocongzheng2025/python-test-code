# -*- coding: utf-8 -*-
# 公共请求工具：配置读取 + 登录
import requests
import configparser
import os
from common.log_util import get_logger

logger = get_logger()

# 读取配置
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config = configparser.ConfigParser()
config.read(os.path.join(PROJECT_DIR, "config.ini"), encoding="utf-8")

BASE = config["server"]["base_url"]
USERNAME = config["user"]["username"]
PASSWORD = config["user"]["password"]


def login():
    """登录，返回token"""
    logger.info("登录请求: POST /login (user=%s)", USERNAME)
    resp = requests.post(BASE + "/login", json={"username": USERNAME, "password": PASSWORD})
    logger.info("登录响应: HTTP %s", resp.status_code)
    return resp.json()["token"]
