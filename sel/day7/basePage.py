# Time:2020-02-21 15:07
# Author:TSL

#PO是什么？
# 面向对象的特性：封装、继承、多态，在自动化中一样适用，Selenium自动化测试中的
# PageObject，通过PO模式可以大大提高测试用例的维护效率。


from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
#显示等待需要导入的库

class BasePage:
    def __int__(self,driver,url):
        self.driver = driver
        self.url = url

    def open(self,page_title):
        """
        打开网址，如果传入的page_title与网页的title不同触发断言
        page_title  网页的标题
        :return:
        """
        self.driver.get(self.url)
        assert  page_title in self.driver.title

    def find_element(self,locator,timeout):
        """
        重写一个寻找元素的方法
        :param locator:
        :param timeout:
        :return:
        """
        try:
            return WebDriverWait(self.driver,timeout).until(
                ec.visibility_of_element_located(
                    locator
                )
            )
        except:
            raise "寻找元素失败，定位方式:{}".format(locator)

    def send_keys(self,webElement,keys):
        webElement.clear()
        webElement.send_keys(keys)























































