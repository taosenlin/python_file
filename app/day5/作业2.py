# coding:utf8
# Time:2020-04-26 13:49
# Author:TSL

import time

from appium import webdriver

desired_caps = {
    'platformName':'Android',
    'platformVersion':'10',
    'deviceName':'wv0426',
    'appPackage':'com.example.jcy.wvtest',
    'appActivity':'.MainActivity',
    'chromedriverExecutableDir':r'D:\tools',
    'noReset':True,
    'newCommandTimeout':6000,
    'skipServerInstallation':True
}

driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(10)

print(driver.current_context)
if driver.current_context == 'NATIVE_APP':
    driver.switch_to.context('WEBVIEW_com.example.jcy.wvtest')
print(driver.current_context)

driver.find_element_by_id('index-kw').send_keys('松勤\n')
res = driver.find_element_by_css_selector('#results>div:nth-child(1) header')
print(res.text)

print(driver.current_context)

driver.switch_to.context('NATIVE_APP')
print(driver.current_context)

driver.find_element_by_accessibility_id('通知').click()



time.sleep(3)
driver.quit()


























































































