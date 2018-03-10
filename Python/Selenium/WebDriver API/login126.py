# coding=utf-8
# sina 邮箱登录
from selenium import webdriver
# 引入Keys模块
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://mail.e-lead.cn:88/")


driver.find_element_by_id("username").clear()
driver.find_element_by_id("username").send_keys("username")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("password")
driver.find_element_by_id("password").send_keys(Keys.ENTER)

driver.quit()