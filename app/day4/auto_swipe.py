#导包
import time

from appium import webdriver

#准备自动化配置信息
desired_caps={
    #移动设备平台
    'platformName':'Android',
    #平台OS版本号,写整数位即可
    'plathformVersion':'8',
    #设备的名称--值可以随便写
    'deviceName':'test0106',
    #提供被测app的信息-包名，入口信息
    'appPackage':'com.hpbr.bosszhipin',
    'appActivity':'.module.launcher.WelcomeActivity',
    #如果被测应用没有安装到手机上,可以指定apk的在电脑上路径
    # 'app':r'D:\apk\xxx.apk',
    #确保自动化之后不重置app
    'noReset':True,
    #设置session的超时时间，单位秒
    'newCommandTimeout':6000,
    #如果不想每次都安装UI2驱动，可以这么设置
    # 'skipServerInstallation':True
}

#初始化driver对象-用于控制手机
driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(10)#稳定元素

#滑动swipe方法
start_x=500
start_y=1700
end_x=start_x
end_y=start_y-500#终点Y坐标等于起点减去滑动的距离
time.sleep(5)
#正常效果
# driver.swipe(start_x,start_y,end_x,end_y)
#惯性效果,当滑动距离很长，滑动时间很短会出现惯性效果
# driver.swipe(start_x,start_y,end_x,end_y,200)

#连续滑动
# for i in range(9):
#     driver.swipe(start_x, start_y, end_x, end_y,500)
#     #边滑动边找元素信息
#     job_msg = driver.find_element_by_id('com.hpbr.bosszhipin:id/tv_position_name')
#     print(job_msg.text)


#打开通知
driver.open_notifications()

#收起通知栏
#1.向上推
#2.可以利用返回建
time.sleep(5)
#模拟按键操作
driver.press_keycode(4)

#模拟音量调节
time.sleep(2)
#增大音量
for i in range(9):
    driver.press_keycode(24)

time.sleep(1)
#减小音量
for i in range(9):
    driver.press_keycode(25)

time.sleep(5)

driver.quit()