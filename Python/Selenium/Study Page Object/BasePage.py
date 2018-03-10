# coding=utf-8
"""
Created on 2017-09-10
@author: Ken
Project: 基础类BasePage，封装所有页面都共有的方法
"""
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    """
    定义open方法
    重定义find_element, switch_frame, send_keys等方法
    """

    def __init__(self, selenium_driver, base_url, pagetitle):
        self.driver = selenium_driver
        self.base_url = base_url
        self.pagetitle = pagetitle

    # 定义on_page方法，判断打开页面的title是否和配置的title相同
    def on_page(self, pagetitle):
        return pagetitle in self.driver.title

    # 定义_open方法，调用on_page判断打开的页面和预期的页面一致
    def _open(self, url, pagetitle):
        # 调用get方法打开网页
        self.driver.get(url)
        self.driver.maximize_window()
        assert self.on_page(pagetitle), u"打开页面失败 %s" % url

    # 调用_open打开页面
    def open(self):
        self._open(self.base_url, self.pagetitle)

    # 重定义find_element
    def find_element(self, *loc):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            print(u"%s 页面找不到元素 %s" % (self, loc))

    # 重写switch_frame方法
    def switch_frame(self, *loc):
        return self.driver.switch_to.frame(loc)

    # 定义script方法
    def script(self, src):
        self.driver.execute_script(src)

    # 判断alert是否存在，存在则打印对话框内容，并接受
    def is_alert(self):
        alert = EC.alert_is_present()(self.driver)
        if alert:
            alert_str = self.driver.switch_to.alert().text
            print(alert_str)
            alert_str.acept()
        else:
            print(u"找不到alert")

    # 重写send_keys方法
    def send_keys(self, loc, value, clear_first=True, click_first=True):
        try:
            loc = getattr(self, "_%s" % loc)
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(value)
        except AttributeError:
            print(u"%s 页面找不到元素 %s" % (self, loc))
