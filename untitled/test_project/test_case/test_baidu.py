#coding : utf8
#Author : taosenlin
#Time : 2020/5/25 14:22

from selenium import webdriver
import unittest
import time

class Testbaidu(unittest.TestCase):

    def setUp(self,url = 'https://www.baidu.com'):
        self.driver = webdriver.Chrome("E:\chromedriver.exe")
        self.url = url

    def tearDown(self):
        self.driver.quit()

    def test_baidu(self):
        # url = 'https://www.baidu.com'
        driver = self.driver
        driver.get(self.url)
        driver.find_element_by_id('kw').clear()
        driver.find_element_by_id('kw').send_keys('unittest')
        driver.find_element_by_id('su').click()
        time.sleep(3)
        title = driver.title
        self.assertEqual(title,'unittest_百度搜索')

if __name__ == '__main__':
    unittest.main()



























































































