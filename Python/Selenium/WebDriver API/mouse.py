# coding=utf-8
from selenium import webdriver
from time import sleep
# 引入ActionChains类
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

# 定位到要悬停的元素
above = driver.find_element_by_link_text("更多产品")
# 对定位到的元素执行悬停操作
ActionChains(driver).move_to_element(above).perform()

# 休眠3秒
sleep(3)

# 定位到要双击的元素
double_click = driver.find_element_by_id("su")
# 对定位到的元素执行双击操作
ActionChains(driver).double_click(double_click).perform()

driver.find_element_by_link_text("hao123").click()
driver.find_element_by_link_text("腾　讯").click()