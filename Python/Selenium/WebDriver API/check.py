# coding=utf-8
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://mail.e-lead.cn:88/")

print('Before login==================')

# 打印当前页面title
title = driver.title
print(title)

# 打印当前页面URL
now_url = driver.current_url
print(now_url)

# 执行邮箱登录
driver.find_element_by_id("username").clear()
driver.find_element_by_id("username").send_keys("xukui")
driver.find_element_by_id("password").clear()
driver.find_element_by_id("password").send_keys("elead2016")
driver.find_element_by_css_selector(".btn_login").click()
sleep(5)

print('After login===================')

# 再次打印当前页面title
title = driver.title
print(title)

# 打印当前页面URL
now_url = driver.current_url
print(now_url)

# 获得登录的用户名
user = driver.find_element_by_xpath("//div[@class='umail-user']/span[1]").text
print(user)

driver.quit()