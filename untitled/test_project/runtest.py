#coding : utf8
#Author : taosenlin
#Time : 2020/5/25 14:22

import unittest
from test_case import test_baidu,test_youdao

#构造测试集
suite = unittest.TestSuite()
suite.addTest(test_baidu.Testbaidu('test_baidu'))
suite.addTest(test_youdao.Testyoudao('test_youdao'))

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite)




























































































