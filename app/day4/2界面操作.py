# Time:2020-03-01 12:26
# Author:TSL

# 一、手机界面操作
# 1、滑动屏幕操作
# (1)Appium WebDriver的swipe方法(坐标和duration)
# (2)直接查看，估算操作坐标
# (3)先获取元素坐标，在分析操作坐标(更健壮)
# (4)location = ele.location  左上角坐标（dict:有x,y）
#    sizel = ele.size  宽、高（dict:有width,height）



# 2、操作不可见元素
# (1)先滑动到其可见
# (2)再操作该元素
# (3)获取全屏幕尺寸
# screenSize = driver.get_window_size()
# screenW = screenSize['width']
# screenH = screenSize['height']



# 3、查看通知操作
# (1)打开通知栏
# 下滑屏幕或driver.open_notifications()

# (2)查看通知内容
# 选择元素操作元素

# (3)返回
# 上滑屏幕或按下返回键



# 4、按键操作
# 使用场景：模拟手机硬件信号，如电源、音量、明暗、键盘等

# 操作方法：driver.press_keycode(keycode)

# 如何找到Keycode： http://developer.android.com/reference/android/view/KeyEvent.html


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
# driver.swipe(start_x,start_y,end_x,end_y,200)    #在200ms内滑动500像素（时间很短时，容易出现惯性效果）

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
#模拟按键操作（返回键）
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




















































