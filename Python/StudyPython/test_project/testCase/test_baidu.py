#!/usr/bin/python
# coding=utf-8
from selenium import webdriver
import unittest


class Baidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path='/Users/xukui/Software/geckodriver')
        self.base_url = "http://www.baidu.com"

    def testbaidu(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("selenium2")
        driver.find_element_by_id("su").click()

    def tearDown(self):
        self.driver.quit()
