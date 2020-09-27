from appium import webdriver

#准备自动化配置信息
desired_caps={
    #移动设备平台
    'platformName':'Android',
    #平台OS版本号,写整数位即可
    'plathformVersion':'8',
    #设备的名称--值可以随便写
    'deviceName':'test0106',
    #直接指定浏览器名称参数为chrome（不需要再指定包名和入口信息）
    'browserName':'Chrome',
    #确保自动化之后不重置app
    'noReset':True,
    #设置session的超时时间，单位秒
    'newCommandTimeout':6000,
    #如果不想每次都安装UI2驱动，可以这么设置
    #指定自动化驱动
    # 'automationName':'UiAutomator2',
    # 'skipServerInstallation':True
    #使用指定的浏览器驱动-匹配手机上的谷歌浏览器
    'chromedriverExecutableDir':r'D:\tools\webdrivers'

}

driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(10)#稳定元素

#操作浏览器内容，接下里可以完全使用selenium的方式去自动化页面

driver.get('https://www.baidu.com/')
#用web查找元素的方式查找手机网页内部元素
driver.find_element_by_id('index-kw').send_keys('松勤')
driver.find_element_by_id('index-bn').click()

res=driver.find_element_by_css_selector('#results>div:nth-child(1) header')

print(res.text)


driver.quit()

