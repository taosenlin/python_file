#coding : utf8
#Author : taosenlin
#Time : 2020/5/25 14:22

from selenium import webdriver
import unittest
import time

class Testyoudao(unittest.TestCase):

    def setUp(self,url = 'http://www.youdao.com'):
        self.driver = webdriver.Chrome("E:\chromedriver.exe")
        self.url = url

    # def tearDown(self):
    #     self.driver.quit()

    def test_youdao(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.get(self.url)
        driver.find_element_by_id('translateContent').clear()
        driver.find_element_by_id('translateContent').send_keys('你好')
        driver.find_element_by_id('translateContent').submit()
        time.sleep(3)
        # all_handles = driver.window_handles
        # print(all_handles)
        # ['CDwindow-532A1181B47176FD6B1EED30A143D819']
        driver.find_element_by_css_selector('.close.js_close').click()
        time.sleep(5)
        page_source = driver.page_source
        print(page_source)
        self.assertIn('hello',page_source)


if __name__ == '__main__':
    unittest.main()






































































































