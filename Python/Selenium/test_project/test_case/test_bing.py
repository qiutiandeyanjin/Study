# coding=utf-8
from selenium import webdriver
import unittest
import time


class Bing(unittest.TestCase):
    u"""Bing搜索测试"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = "http://cn.bing.com/"

    def test_bing(self):
        u"""搜索关键字：webdriver"""
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("sb_form_q").clear()
        driver.find_element_by_id("sb_form_q").send_keys("webdriver")
        driver.find_element_by_id("sb_form_go").click()
        time.sleep(2)
        title = driver.title
        self.assertEqual(title, u"webdriver - 国内版 Bing")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
