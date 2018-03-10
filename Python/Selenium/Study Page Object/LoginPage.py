# coding=utf-8
"""
Created on 2017-09-10
@author: Ken
Project: 调用BasePage类，封装input_username, input_password, click_submit
"""
from selenium.webdriver.common.by import By
from BasePage import BasePage


class LoginPage(BasePage):
    # 元素定位器
    username_loc = (By.ID, "account")
    password_loc = (By.NAME, "password")
    submit_loc = (By.ID, "submit")
    userid_loc = (By.ID, "userMenu")

    # 通过继承覆盖（Overriding）方法：如果子类和父类的方法名相同，优先用子类自己的方法
    def open(self):
        # 调用BasePage中的_open方法
        self._open(self.base_url, self.pagetitle)

    # 定义input_username
    def input_username(self, username):
        self.find_element(*self.username_loc).send_keys(username)

    # 定义input_password
    def input_password(self, password):
        self.find_element(*self.password_loc).send_keys(password)

    # 定义click_submit
    def click_submit(self):
        self.find_element(*self.submit_loc).click()

    # 登录成功查找user_id
    def show_userid(self):
        return self.find_element(*self.userid_loc).text
