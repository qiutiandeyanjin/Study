# !/usr/bin/python3

"""
FileName    : Log.py
Author      : ken
Date        : 2018-04-16
Describe    : Log demo
"""

import logging.config
import os
import threading

import yaml

currentPath = os.path.split(os.path.realpath(__file__))[0]


class Log:
    """set logging config"""

    logging_config = os.path.join(currentPath, "logging.yaml")
    logs_path = os.path.join(currentPath, "logs")
    if not os.path.exists(logs_path):
        os.mkdir(logs_path)

    def __init__(self,
                 default_path=logging_config,
                 default_level=logging.INFO,
                 env_key="LOG_CFG"):
        self.default_path = default_path
        self.default_level = default_level
        self.env_key = env_key
        self.logger = None

    def __set_logger(self):
        """
        set logger
        :return: None
        """
        path = self.default_path
        value = os.getenv(self.env_key, None)
        if value:
            path = value
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                logging.config.dictConfig(yaml.load(f))
        else:
            logging.basicConfig(level=self.default_level)

    def get_logger(self):
        """
        get logger
        :return: logger
        """
        self.__set_logger()
        self.logger = logging.getLogger('fileLogger')
        return self.logger


class MyLog:
    log = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_log():
        if MyLog.log is None:
            MyLog.mutex.acquire()
            MyLog.log = Log()
            MyLog.mutex.release()
        return MyLog.log


if __name__ == "__main__":
    log = MyLog.get_log()
    logger = log.get_logger()
    logger.debug("test debug")
    logger.info("test info")
