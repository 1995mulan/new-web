from selenium import webdriver
browser = webdriver.Chrome()  #打开浏览器

这是之前的驱动调用



# 前台开启浏览器模式
def openChrome():
    # 加启动配置
    option = webdriver.ChromeOptions()
    option.add_argument('disable-infobars')
    # 打开chrome浏览器
    driver = webdriver.Chrome(chrome_options=option)
    return driver

# 访问web界面
def operationAuth(driver):
    
    url = "https://192.168.10.231"
    driver.get(url)
#web界面修改登录密码   
    driver.find_element_by_name("changePwd").click()
    
    
