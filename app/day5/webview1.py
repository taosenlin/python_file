# coding=utf8
from appium import webdriver
import time
import traceback
 
desired_caps = {
    # 'automationName': 'UiAutomator2',
    'platformName': 'Android',
    'platformVersion': '8',
    'deviceName': 'test',
    'appPackage': 'com.example.jcy.wvtest',
    'appActivity': '.MainActivity',
    # 'unicodeKeyboard': True,
    # 'resetKeyboard':True,
    'chromedriverExecutableDir':r'D:\tools\webdrivers\chromedriver_win32_v2.38',
    'noReset': True,
    'newCommandTimeout': 6000
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps) #启动Remote RPC
driver.implicitly_wait(10)

#操作原始应用里的webview
try:
    # -----------------------
    time.sleep(3)

    # driver.find_element_by_accessibility_id('习近平谋划推动的这项国家战略5年了 置顶 央视网新闻').click()

    print(driver.contexts)
    print(driver.current_context)

    driver.switch_to.context('WEBVIEW_com.example.jcy.wvtest')

    print(driver.current_context)

    # ai_ele=driver.find_element_by_custom('ai:index-kw')
    # print(ai_ele.text)

    driver.find_element_by_id('index-kw').send_keys('松勤\n')

    # driver.find_element_by_id('index-bn').click()

    driver.switch_to.context('NATIVE_APP')
    print(driver.current_context)

    driver.find_element_by_id('navigation_dashboard').click()
    time.sleep(2)
    driver.find_element_by_id('navigation_notifications').click()

    # -----------------------

except:
    print(traceback.format_exc())

input('**** Press to quit..')
driver.quit()