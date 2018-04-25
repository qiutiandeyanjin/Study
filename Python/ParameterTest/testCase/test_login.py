# !/usr/bin/python3

"""
FileName    : test_login.py
Author      : ken
Date        : 2018-04-21
Describe    : user the paramUnittest, test login
"""
import os
import time
import unittest
from time import sleep

import paramunittest
from selenium import webdriver

from commonFile import getDir
from commonFile.common import get_excel_value

proDir = getDir.proDir
now = time.strftime("%Y_%m_%d %H:%M:%S")
loginCase = get_excel_value("loginCase.xls", "login_test")


@paramunittest.parametrized(*loginCase)
class LoginTest(unittest.TestCase):
    def setParameters(self, case_num, case_name, username, password, excepted):
        """
        从 excel 中获取用例
        :param case_num: 用例编码
        :param case_name: 用例名称
        :param username: 用户名
        :param password: 密码
        :param excepted: 期望值
        :return:
        """
        self.case_num = case_num
        self.case_name = case_name
        self.username = username
        self.password = password
        self.excepted = excepted

    def setUp(self):
        self.baseUrl = "http://www.mi.com"
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)  # 静默等待10s

    def test_login(self):
        self._testMethodDoc = self.case_name  # 设置用例名称
        driver = self.driver
        driver.get(self.baseUrl)
        driver.find_element_by_xpath("//div[@class='topbar-info']/a[1]").click()
        sleep(2)
        driver.find_element_by_css_selector("[id='username']").clear()
        driver.find_element_by_css_selector("[id='username']").send_keys(self.username)
        driver.find_element_by_css_selector("[id='pwd']").clear()
        driver.find_element_by_css_selector("[id='pwd']").send_keys(self.password)
        driver.find_element_by_css_selector("[class='btns_bg']>input").click()
        sleep(1)
        # 获取登录错误信息
        error_msg = driver.find_element_by_css_selector("#login-main-form > div > "
                                                        "div.err_tip > div > span").text
        self.assertEqual(error_msg, self.excepted)

    def get_screenshot(self):
        file_path = os.path.join(proDir, "testFile", "shots")
        if not os.path.exists(file_path):
            os.mkdir(file_path)
        shot_name = "%s_%s.png" % (self.case_num, now)
        shot_path = os.path.join(proDir, file_path, shot_name)
        self.driver.get_screenshot_as_file(shot_path)

    def tearDown(self):
        self.get_screenshot()
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
