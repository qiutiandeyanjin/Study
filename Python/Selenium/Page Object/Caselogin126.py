# coding=utf-8
"""
Created on 2017-09-03
@author: Ken
Project: 使用unittest框架编写测试用例
"""
import unittest
from LoginPage import LoginPage
from selenium import webdriver


class CaseLogin126mail(unittest.TestCase):
    """
    登录126邮箱的case
    """

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.url = "http://mail.126.com"
        self.username = "qiutiandeyanjin@126.com"
        self.password = "89757xutingyu"

    # 用例执行体
    def test_login_mail(self):
        # 声明LoginPage类对象
        login_page = LoginPage(self.driver, self.url, u"网易")
        # 调用打开页面组件
        login_page.open()
        # 切换到登录框Frame
        login_page.switch_frame('x-URS-iframe')
        # 调用用户名输入组件
        login_page.input_username(self.username)
        # 调用密码输入组件
        login_page.input_password(self.password)
        # 调用点击登录按钮组件
        login_page.click_submit()

    def tearDown(self):
        self.driver.quit()


if __name__ == "main":
    unittest.main()
