# coding=utf-8
"""
Created on 2017-09-10
@author: Ken
Project: 调用LoginPage, 使用unittest编写禅道登录测试用例
"""
import unittest
from selenium import webdriver
from LoginPage import LoginPage
from time import sleep


class login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.url = "http://ken.huawei.com/zentaopms/www/index.php"
        self.username = "xwx406368"
        self.password = "tiyudesi12"

    def test_login(self):
        """
        Project: 调用LoginPage
        :return:
        """
        login_page = LoginPage(self.driver, self.url, u"用户登录 - 禅道")
        login_page.open()
        login_page.input_username(self.username)
        login_page.input_password(self.password)
        login_page.click_submit()
        sleep(3)
        login_page.is_alert()
        print(str(login_page.show_userid()))

    def tearDown(self):
        self.driver.quit()
