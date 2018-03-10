# coding=utf-8
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://m.mail.10086.cn")

# 参数数字为像素点
print("设置浏览器宽 480、高 800 显示")
driver.set_window_size(480, 800)
driver.quit()