# Time:2020-02-17 14:08
# Author:TSL

# iframe,又叫浮动帧标记，是内嵌的网页元素，可以将一个html文件嵌入到另一个html文件中显示

#对iframe进行操作，又以下三种方法：

# switch_to_iframe()       #切换到iframe上
# switch_to.frame()        #切换到iframe上
# switch_to.default_content()    #切换回原主页面

from selenium import webdriver

import time

driver = webdriver.Chrome("D:\\ruanjiananzhuang\chromedriver.exe")
#实例化一个浏览器对象
driver.get("D:\PyCharm\sel\day3\\test.html")
#访问网址

#切换frame
#第一步，要找到frame元素
iframe = driver.find_element_by_id("f91fb5bc-bd95-45bf-bd77-977a2afbd25f")
#切换到对应的frame
driver.switch_to.frame(iframe)  #主流用法

driver.find_element_by_id("e4890ded-16e1-4445-bf8e-7f655793f332").send_keys("哈哈")

#切换到原主页面
driver.switch_to.default_content()

#打印出主页面的 哈哈
print(driver.find_element_by_id("a9dfdf690-ee7e-4e52-80f2-4804a7a6ff50").text)


time.sleep(5)

driver.quit()







































