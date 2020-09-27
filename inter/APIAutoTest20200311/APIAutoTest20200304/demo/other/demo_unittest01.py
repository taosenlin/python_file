import unittest
import time
from lib.courseLib import add,list,delete
from lib.loginLib import login
class UnittestDemo1(unittest.TestCase):


    #第二对方式-【类级别】
    @classmethod
    def setUpClass(cls):
        cls.sessionID=login('auto','sdfsdfsdf')
        cls.clearDate()

    @classmethod
    def tearDownClass(cls):
        cls.clearDate()

    @classmethod
    def clearDate(cls):
        listData = list(1, 999,cls.sessionID)
        i = 0
        for item in listData["retlist"]:
            delete(item["id"],cls.sessionID)
            i = i + 1
        print('本次共删除了数据条数：', i)

    #用例1
    def test01(self):
        courseName = '初中化学' + str(int(time.time() * 10000))
        retDict = add(courseName, 'sdfdss', 0,self.sessionID)
        self.assertEqual(retDict['retcode'],0,'测试不通过xxxxx')
        id = retDict['id']
        # 2.调用列出课程接口，查看新增的课程是否存在
        retDict2 = list(1, 500,self.sessionID)
        # print(retDict2['retlist'])
        exit2 = 0
        for item in retDict2['retlist']:
            if id == item['id']:
                exit2 = 1
                break
        self.assertEqual(exit2,1)
        print('测试通过')

    #用例2
    @unittest.skip('这里写不执行的原因')
    def test02(self):
        print('>>>>测试用例2运行了')

    #用例3
    def test03(self):
        print('>>>>测试用例3运行了')

    #用例4
    def test04(self):
        print('>>>>测试用例4运行了')


