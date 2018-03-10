# coding=utf-8
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.youdao.com")

# 获取cookie信息
cookie = driver.get_cookies()

# 向cookies中的name和value中添加会话信息
driver.add_cookie({'name': 'key-aaaaaaa', 'value': 'value-bbbbbbb'})

# 遍历cookies中的name和value信息并打印，当然还有上面添加的信息
for c in cookie:
    print("%s -> %s" % (c['name'], c['value']))

driver.quit()