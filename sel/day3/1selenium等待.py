# Time:2020-02-14 14:19
# Author:TSL

from selenium import webdriver

import time

#以下导入提供给显式等待使用
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException


driver = webdriver.Chrome("D:\\ruanjiananzhuang\chromedriver.exe")
#创建浏览器实例


# #隐式等待时间（设置一遍之后全局通用）
# #隐式等待定义：隐式等待是在尝试发现某个元素的时候，如果没能立刻发现，就等待固定长度的时间，隐式等待时间应用于脚本中的所有元素
# driver.implicitly_wait(5)


driver.get("http://www.baidu.com")  #访问网址

#搜索松勤
driver.find_element_by_id("kw").send_keys("松勤")
driver.find_element_by_id("su").click()

# time.sleep(5)   #固定等待5秒，等松勤教育页面刷新出来，否则会出现元素定位不到的问题

#显式等待
try:
    #等待元素出现
    ele = WebDriverWait(driver,5).until(ec.presence_of_element_located(
        (By.CSS_SELECTOR,"#\\34 > h3 > a > em")
    )
    ) #松勤教育官网css_selector
    ele.click()
    print("元素找到了")
except TimeoutException:
    print("元素没找到")







# #点击进入松勤教育官网
# driver.find_element_by_css_selector("#\\34  > h3 > a > em").click()






























time.sleep(5)     #加隐式等待后仍然需要设置退出前等待5秒，以免没反应时间看不到现象

driver.quit()