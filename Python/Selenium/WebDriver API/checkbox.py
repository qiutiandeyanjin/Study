# coding=utf-8
from selenium import webdriver
import os,time

driver = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('checkbox.html')
driver.get(file_path)
'''
# 选择页面上所有的tag name为input的元素
inputs = driver.find_elements_by_tag_name('input')

# 然后从中过滤出type为checkbox的元素，单击勾选
for i in inputs:
    if i.get_attribute('type') == 'checkbox':
        i.click()
        time.sleep(1)

driver.quit()
'''

# 通过XPath找到type=checkbox的元素
# checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")

# 通过CSS找到type=checkbox的元素
checkboxes = driver.find_elements_by_css_selector('input[type=checkbox]')
for checkbox in checkboxes:
    checkbox.click()
    time.sleep(1)

# 打印当前页面上type为checkbox的个数
print(len(checkboxes))

# 把页面上最后一个checkbox的钩给去掉
driver.find_elements_by_css_selector('input[type=checkbox]').pop().click()
time.sleep(1)

driver.quit()