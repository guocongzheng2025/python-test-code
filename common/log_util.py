# -*- coding: utf-8 -*-
# 日志工具：跑测试时自动记录过程，方便出问题时排查
import logging
import os

# logs/ 目录
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_DIR = os.path.join(PROJECT_DIR, "logs")
os.makedirs(LOG_DIR, exist_ok=True)

logger = logging.getLogger("auto_test")
logger.setLevel(logging.INFO)

# 给logger挂上"文件输出"和"终端输出"（不用basicConfig，避免被pytest干扰）
if not logger.handlers:
    _fmt = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")

    file_handler = logging.FileHandler(os.path.join(LOG_DIR, "test.log"), encoding="utf-8")
    file_handler.setFormatter(_fmt)
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(_fmt)
    logger.addHandler(console_handler)


def get_logger():
    """获取日志器"""
    return logger
