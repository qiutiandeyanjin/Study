from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

now = time.strftime('%Y-%m-%d %H:%I:%S')

print(now)
driver.set_window_size(800, 600)
time.sleep(2)

js = "alert(window.document.title);"

driver.execute_script(js)
time.sleep(2)

alert_str = driver.switch_to.alert.text
print alert_str
driver.switch_to.alert.accept()

js1 = "window.scrollTo(100,450);"

driver.execute_script(js1)

print("test ok")
print now

driver.quit()
