# Time:2020-02-23 22:09
# Author:TSL

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

import time

driver = webdriver.Chrome("D:\\ruanjiananzhuang\chromedriver.exe")
#谷歌浏览器
driver.get("https://www.vmall.com/")
#访问网址

#点击华为官网
driver.find_element_by_link_text("华为官网").click()

def checkHuawei():
    """
    检查华为官网
    :return:
    """
    expected = "手机|笔记本平板|智慧屏|穿戴|更多产品|软件应用|服务与支持|零售店"
    driver.maximize_window()  #窗口最大化
    #考虑到浏览器过于窄小，菜单隐藏的因素

    #匹配每一个菜单元素
    eles = driver.find_elements_by_css_selector(".clearfix.nav-cnt > li")
    eleTexts = [ele.text for ele in eles]
    print("-"*70)
    print("|".join(eleTexts))

###############################################################################

def checkVmall():
    ele = driver.find_element_by_id("zxnav_1")
    ActionChains(driver).move_to_element(ele).perform()  #鼠标悬停到笔记本

    eles = driver.find_elements_by_css_selector("#zxnav_1 .subcate-item>a>p>span")
    #匹配到每一个悬浮菜单中的元素
    eleTexts = [ele.text for ele in eles]
    print("华为官网")
    print("-"*70)
    print("|".join(eleTexts))

###############################################################################


for handle in driver.window_handles:
    driver.switch_to.window(handle)

    if "消费者业务官网" in driver.title:
        checkHuawei()
    else:
        checkVmall()


driver.quit()






















time.sleep(5)

driver.quit()