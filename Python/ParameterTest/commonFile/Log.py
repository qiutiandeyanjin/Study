# !/usr/bin/python3

"""
FileName    : Log.py
Author      : ken
Date        : 2018-04-21
Describe    : logging config
"""

import datetime
import logging
import os
import sys
import threading

from commonFile import getDir

proDir = getDir.proDir
now = datetime.datetime.now().strftime("%Y_%m_%d")


class Log:
    """logging config and format
        1. set_logger
        2. get_logger
    """

    LogFile = os.path.join(proDir, "logs")
    if not os.path.exists(LogFile):
        os.mkdir(LogFile)

    LogName = "parameterTest_%s.log" % now

    def __init__(self):
        self.log_path = os.path.join(self.LogFile, self.LogName)
        # define handler
        self.logger = logging.getLogger()
        self.logger.setLevel(level=logging.INFO)
        handler = logging.FileHandler(self.log_path, encoding="utf-8")
        # define format
        formatter = logging.Formatter(fmt="%(asctime)s %(filename)s[line:%(lineno)d] "
                                          "%(levelname)s %(message)s",
                                      datefmt="%a, %b %Y %H:%M:%S")
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

    def get_logger(self):
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
    logger = MyLog.get_log().get_logger()
    logger.info("test info")
    logger.debug("test debug")
    logger.error("test error")
    logger.critical("test critical")
