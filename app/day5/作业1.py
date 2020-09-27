# coding:utf8
# Time:2020-04-25 22:04
# Author:TSL

import time

from appium import webdriver

desired_caps = {
    'platformName':'Android',
    'platformVersion':'10',
    'deviceName':'toutiao',
    'appPackage':'io.manong.developerdaily',
    'appActivity':'io.toutiao.android.ui.activity.LaunchActivity',
    'noReset':True,
    'newCommandTimeout':6000,
    'skipServerInstallation':True
}

driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(10)

xpath = '//*[@resource-id="io.manong.developerdaily:id/home_feature_recycler_view"]/android.widget.LinearLayout[1]//android.widget.RelativeLayout//android.widget.TextView'

t = driver.find_element_by_xpath(xpath)
t1 = t.text
t.click()

t2 = driver.find_element_by_id("io.manong.developerdaily:id/tv_title")
assert t2.text == t1

driver.press_keycode(4)

ele = driver.find_element_by_id('io.manong.developerdaily:id/imageView')
if ele:
    print('success')


time.sleep(3)
driver.quit()
























































































