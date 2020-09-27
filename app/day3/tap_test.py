#导包
import time

from appium import webdriver

#准备自动化配置信息
desired_caps={
    #移动设备平台
    'platformName':'Android',
    #平台OS版本号
    'plathformVersion':'8',
    #设备的名称--值可以随便写
    'deviceName':'test0106',
    #提供被测app的信息-包名，入口信息
    'appPackage':'com.alpha.lagouapk',
    'appActivity':'.HelloActivity',
    #确保自动化之后不重置app
    'noReset':True,
    #设置session的超时时间，单位秒
    'newCommandTimeout':6000,
    #指定自动化驱动
    #'automationName':'UiAutomator1',

}

#初始化driver对象-用于控制手机
driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(10)#稳定元素

#等待目标区域出现
time.sleep(5)

#根据坐标点击操作
# driver.tap([(550,2060)])


#根据相对坐标来操作，

#先获取屏幕的尺寸
size=driver.get_window_size()
width=size['width']
height=size['height']

pos_x=width/2
pos_y=int(height*0.926)

driver.tap([(pos_x,pos_y)])

time.sleep(5)



driver.quit()


