# coding:utf8
# Time:2020-04-19 16:20
# Author:TSL

#导包
from appium import webdriver

#准备自动化配置信息
desired_caps={
    #移动平台设备
    'platformName':'Android',
    #平台os版本，写整数位即可
    'platformVersion':'10',
    #设备名称--值可以随便写
    'deviceName':'tslPhone',
    #提供被测app的信息-包名，入口信息
    'appPackage':'com.ibox.calculators',
    'appActivity':'com.ibox.calculators.SplashActivity',
    #确保自动化之后不重置app
    'noReset':True,
    #设置session的超时时间，单位为--秒
    'newCommandTimeout':6000
}

#初始化driver对象，用于控制手机
driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)
driver.implicitly_wait(10)  #用于稳定元素

driver.find_element_by_id('com.ibox.calculators:id/digit3').click()
driver.find_element_by_id('com.ibox.calculators:id/plus').click()
driver.find_element_by_id('com.ibox.calculators:id/digit9').click()
driver.find_element_by_id('com.ibox.calculators:id/equal').click()
driver.find_element_by_id('com.ibox.calculators:id/mul').click()
driver.find_element_by_id('com.ibox.calculators:id/digit5').click()
driver.find_element_by_id('com.ibox.calculators:id/equal').click()
num = driver.find_element_by_id('com.ibox.calculators:id/cv')
nums = num.find_elements_by_class_name('android.widget.TextView')
res = nums[1].text

if res == '60':
    print(res)
    print('测试通过')
else:
    print('测试不通过')


driver.quit()






















































































