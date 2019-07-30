# encoding=utf8

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time
import paramiko


#开启谷歌浏览器
driver = webdriver.Chrome()

#web界面上传授权文件
driver.get("https://192.168.10.231")
#登录
driver.find_element_by_id("password").send_keys("111111")
driver.find_element_by_name("loginBtn").click()
 
# 切到系统界面
time.sleep(1)
driver.find_element_by_name("tab.system").click()
#设备授权
button2=driver.find_element_by_name("secsmartsys.device.authorization")
driver.execute_script("$(arguments[0]).click()",button2)
time.sleep(1)
driver.find_element_by_id("cert_file").send_keys("C:/ff/authorization.license")
time.sleep(1)
driver.find_element_by_id("cert_key").send_keys("C:/ff/private.key")
time.sleep(1)
driver.find_element_by_name("secsmartsys.authorization").click()

