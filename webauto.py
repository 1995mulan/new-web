# encoding=utf8

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time
import paramiko
import zipfile
import os
import stat


#调用安装脚本
str0=('python anzhuang.py')
p0=os.system(str0)
print(p0)



#开启谷歌浏览器
driver = webdriver.Chrome()

driver.get("https://192.168.10.231")
time.sleep(1)

#web界面修改登录密码并回到登录界面   
driver.find_element_by_name("changePwd").click()
driver.find_element_by_id("password").send_keys("123456")    
driver.find_element_by_id("newPassword").send_keys("111111")   
driver.find_element_by_id("passwordConfirm").send_keys("111111")
driver.find_element_by_name("loginChange").click()
driver.find_element_by_name("returnLogin").click()
#登录
time.sleep(1)
driver.find_element_by_id("password").send_keys("111111")
driver.find_element_by_name("loginBtn").click()
   
 
# 切到系统界面
time.sleep(1)
driver.find_element_by_name("tab.system").click()
# web界面生成下载授权文件    
button=driver.find_element_by_name("secsmartsys.create.the.certificate")
driver.execute_script("$(arguments[0]).click()",button)
time.sleep(1)
button1=driver.find_element_by_name("secsmartsys.download.the.certificate")
driver.execute_script("$(arguments[0]).click()",button1)
time.sleep(1)
    
#解压授权文件到c盘的dd目录下
os.chdir ('C:/Users/Administrator/Downloads')
extracting = zipfile.ZipFile('authorization.zip')
extracting.extractall('C:/dd')
    

# 授权系统生成授权文件
#driver.get("http://192.168.10.28")

driver.find_element_by_css_selector("#strategy-right > div > div.pull-right > button.btn.btn-default.btn-primary1").click()
time.sleep(1)
driver.find_element_by_id("authorization_file").send_keys("C:/dd/devinfo.data")
driver.find_element_by_id("key_file").send_keys("C:/dd/test.key")
time.sleep(1)
button3=driver.find_element_by_css_selector("#t4_authorization > tbody > tr:nth-child(3) > td > button")
driver.execute_script("$(arguments[0]).click()",button3)
driver.find_element_by_id("customer").send_keys("客户工控3")
  
js = 'document.getElementById("expiredTime").removeAttribute("readonly");'
driver.execute_script(js)
js_value = 'document.getElementById("expiredTime").value="2099-12-10"'
driver.execute_script(js_value)
js1 = 'document.getElementById("maintenanceExpiredTime").removeAttribute("readonly");'
driver.execute_script(js1)
js_value1 = 'document.getElementById("maintenanceExpiredTime").value="2099-12-10"'
driver.execute_script(js_value1)

driver.find_element_by_id("instanceNum").send_keys("10000")
button4=driver.find_element_by_id("audit")
driver.execute_script("$(arguments[0]).click()",button4)
driver.find_element_by_id("authorization").click()

time.sleep(1)

# 授权系统条件查询
          

driver.find_element_by_css_selector("#strategy-right > div > div.pull-right > button.btn.btn-success.btn-primary1").click()
time.sleep(1)
    
driver.find_element_by_id("customer").send_keys("客户工控3")
button5=driver.find_element_by_css_selector("#dialog > div.btn-fix > button.btn.btn-success.btn-primary1")
driver.execute_script("$(arguments[0]).click()",button5)
td = driver.find_element_by_css_selector("#authorized_list > tr > td:nth-child(1)").text
time.sleep(5)    


#ssh登陆下载文件

# 定义一个类，表示一台远端linux主机
class Linux(object):
    # 通过IP, 用户名，密码，超时时间初始化一个远程Linux主机
    def __init__(self, ip, username, password, timeout=30):
        self.ip = ip
        self.username = username
        self.password = password
        self.timeout = timeout
        # transport和chanel
        self.t = ''
        self.chan = ''
        # 链接失败的重试次数
        self.try_times = 3

    # 调用该方法连接远程主机
    def connect(self):
         pass

    # 断开连接
    def close(self):
        pass

    # 发送要执行的命令
    def send(self, cmd):
        pass

    # get单个文件
    def sftp_get(self, remotefile, localfile):
        t = paramiko.Transport(sock=(self.ip, 22))
        t.connect(username=self.username, password=self.password)
        sftp = paramiko.SFTPClient.from_transport(t)
        sftp.get(remotefile, localfile)
        t.close()

    # put单个文件
    def sftp_put(self, localfile, remotefile):
        t = paramiko.Transport(sock=(self.ip, 22))
        t.connect(username=self.username, password=self.password)
        sftp = paramiko.SFTPClient.from_transport(t)
        sftp.put(localfile, remotefile)
        t.close()


if __name__ == '__main__':
    remotefile = r'/home/secsmart/license/%s/authorization.license'%td
    remotefile0 = r'/home/secsmart/license/%s/private.key'%td
    localfile = r'C:/ff/authorization.license'
    localfile0 = r'C:/ff/private.key'
    
    host = Linux('192.168.10.28', 'root', 'root')


    # 将远端的xxoo.txt get到本地，并保存为ooxx.txt
    host.sftp_get(remotefile, localfile)
    host.sftp_get(remotefile0, localfile0)
    
    # # 将本地的xxoo.txt put到远端，并保持为xxoo.txt
    # host.sftp_put(localfile, remotefile)

#调用授权脚本
str=('python shouquan.py')
p=os.system(str)
print(p)
 





'''
# 切到资产界面
    time.sleep(1)
    driver.find_element_by_name("tab.asset").click()
    time.sleep(1)
# 添加多个资产
    i=30   
    while i<100:
        dbname = 'SQLGROUP' + str(i)
        driver.find_element_by_name("common.add").click()
        time.sleep(1) 
        driver.find_element_by_id("dbName").send_keys(dbname)
#        driver.find_element_by_id("dbIp").send_keys(dbname)
#        driver.find_element_by_id("dbPort").send_keys("3306")
#        Select(driver.find_element_by_name("dbTypeName")).select_by_visible_text("MYSQL")
        driver.find_element_by_name("common.submit").click()
        i = i +1
        time.sleep(1)

'''
"""# 切到策略界面
    time.sleep(1)
    driver.find_element_by_name("tab.strategy").click()
    time.sleep(1)
# 添加白名单    
    driver.find_element_by_name("common.btn_add").click()
    time.sleep(1)
    driver.find_element_by_id("name").send_keys("IP")
    driver.find_element_by_css_selector("#addWhiteList > table > tbody > tr:nth-child(8) > td:nth-child(2) > span > span.selection > span > ul > li > input").send_keys("192.168.10.101")
    driver.find_element_by_css_selector("#addWhiteList > table > tbody > tr:nth-child(8) > td:nth-child(2) > span > span.selection > span > ul > li > input").send_keys(Keys.ENTER)
    driver.find_element_by_name("common.btn_sub").click()
    time.sleep(1)
# 添加黑名单    
    driver.find_element_by_name("strategy.blacklist").click()
    time.sleep(1)
    driver.find_element_by_name("common.btn_add").click()
    time.sleep(1)
    driver.find_element_by_id("name").send_keys("IP")
    driver.find_element_by_css_selector("#addWhiteList > table > tbody > tr:nth-child(8) > td:nth-child(2) > span > span.selection > span > ul > li > input").send_keys("192.168.10.101")
    driver.find_element_by_css_selector("#addWhiteList > table > tbody > tr:nth-child(8) > td:nth-child(2) > span > span.selection > span > ul > li > input").send_keys(Keys.ENTER)
    driver.find_element_by_name("common.btn_sub").click()
    time.sleep(1)
# 添加自定义    
    driver.find_element_by_name("strategy.custom").click()
    time.sleep(1)
    driver.find_element_by_name("common.btn_add").click()
    time.sleep(1)
    driver.find_element_by_id("rule_name").send_keys("IP")
    time.sleep(1)
    driver.find_element_by_css_selector("#select2-risk_type-container > span").click() 
    driver.find_element_by_css_selector("body > span > span > span.select2-search.select2-search--dropdown > input").send_keys("批量修改")
    driver.find_element_by_css_selector("body > span > span > span.select2-search.select2-search--dropdown > input").send_keys(Keys.ENTER)
    driver.find_element_by_css_selector("#t-add-rule > tbody > tr:nth-child(9) > td:nth-child(2) > span > span.selection > span > ul > li > input").send_keys("192.168.10.101")
    driver.find_element_by_css_selector("#t-add-rule > tbody > tr:nth-child(9) > td:nth-child(2) > span > span.selection > span > ul > li > input").send_keys(Keys.ENTER)
    driver.find_element_by_name("common.btn_sub").click()

"""







#print('查询操作完毕！')
 




#    driver.find_element_by_id("dbLoginAccount").send_keys("root")
#    driver.find_element_by_id("dbLoginPwd").send_keys("123456")
   

    
   # elem1 = driver.find_element_by_id("dialog")
   # elem1.send_keys("分组1")

   # driver.find_element_by_xpath("//*[@id="operate-log-right"]/div/div[3]/div/button[2]/label").click()
   # form = find_element_by_name('secsmartsys.device.configuration')
   # form.submit()
    


    




# 方法主入口
#if __name__ == '__main__':
    # 加启动配置
#    driver = openChrome()
#    operationAuth(driver)
