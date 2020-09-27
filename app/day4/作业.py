# coding:utf8
# Time:2020-04-22 22:25
# Author:TSL

import time

from appium import webdriver

desired_caps={
    'platformName':'Android',
    'platformVersion':'10',
    'deviceName':'test0422',
    'appPackage':'com.sqauto',
    'appActivity':'com.sqauto.MainActivity',
    'noReset':True,
    'newCommandTimeout':6000,
    'skipServerInstallation':True
}

driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(10)  #稳定元素

screenSize = driver.get_window_size()
screenW = screenSize['width']
screenH = screenSize['height']
start_x = int(screenW * 0.5)
start_y = int(screenH * 0.80)
end_x = start_x
end_y = int(screenH * 0.2)
driver.implicitly_wait(1)

while True:
    driver.swipe(start_x,start_y,end_x,end_y,1000)
    eles = driver.find_elements_by_accessibility_id('best reputation')
    driver.implicitly_wait(1)

    if not eles:
        continue
    driver.swipe(start_x,eles[0].location['y'], end_x, end_y, 2000)
    break

xpath = "//android.widget.ScrollView//android.widget.ImageView/following-" \
        "sibling::android.widget.TextView[1] | //*[@content-desc='best reputation']"
eleS = driver.find_elements_by_xpath(xpath)
# for ele in eleS:
#     print(ele.text)
eleText = [ele.text for ele in eleS]
# print(eleText)
startN = eleText.index('口碑最佳')
print('\n口碑最佳应用为:\n' + '\n'.join(eleText[startN+1:startN+1+5]))


driver.implicitly_wait(10)
driver.quit()
























































































