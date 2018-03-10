# coding=utf-8
from selenium import webdriver
# 引入ActionChains类
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("http://yunpan.360.cn")
driver.maximize_window()

# 定位到右击的元素
right_click = driver.find_element_by_css_selector(".quc-input-bg")
# 对定位到的元素执行鼠标右键操作
ActionChains(driver).context_click(right_click).perform()

