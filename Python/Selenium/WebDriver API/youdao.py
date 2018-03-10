# coding=utf-8
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.youdao.com")

driver.find_element_by_xpath("//div[@id='border']/input[2]").send_keys("hello")

# 提交输入框的内容
driver.find_element_by_link_text('翻译').click()

driver.quit()