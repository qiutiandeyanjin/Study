#!/usr/bin/python
# coding=utf-8
from selenium import webdriver
from time import sleep
import unittest


class Bing(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "http://cn.bing.com"

    def testbing(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("sb_form_q").clear()
        driver.find_element_by_id("sb_form_q").send_keys("Apple")
        driver.find_element_by_id("sb_form_go").click()
        sleep(2)
        driver.execute_script("alert(\"test ok!\")")
        sleep(2)

    def tearDown(self):
        self.driver.quit()
