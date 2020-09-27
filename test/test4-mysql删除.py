# coding:utf8
# Time:2020-06-24 22:45
# Author:TSL

import unittest
import MySQLdb

class TestClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls):      #连接数据库作初始化操作

        db = MySQLdb.connect(host='192.168.3.14',username='root',password='123456',port=3306,db='plesson',charset='utf8')
        #创建数据库连接

        cu = db.cursor()
        #创建游标

        # sql='''insert into sq_course values
        # ('sql课程1','sql课程描述',1),
        # ('sql课程2','sql课程描述',1);
        # '''

        sql1 = "insert into sq_course(name,`desc`,display_idx) values"

        sql2 = ""
        for i in range(10):
            if i == 9:
                sql2 = """('sql课程{}','sql课程描述',1);""".format(i)
                break
            sql2 = """('sql课程{}','sql课程描述',1),""".format(i)
            sql2 += "\n"

        sql = sql1 + sql2

        cu.execute(sql)
        #执行sql语句

        db.commit()  #涉及到数据库的增删改,都需要使用db去提交修改

        cu.close()
        db.close()


    def testAdd(self):            #测试用例
        assert 1 == 1


    @classmethod
    def tearDownClass(cls):        #连接数据库作数据清除工作

        db = MySQLdb.connect(host='192.168.3.14',username='root',password='123456',port=3306,db='plesson',charset='utf8')
        #创建数据库连接

        cu =db.cursor()
        #创建数据库游标

        sql = """
        delete * from sq_course where 
        name like '%课程%';
        
        """

        cu.execute(sql)
        #执行sql语句

        db.commit()
        #数据库涉及增删改,都需要使用db提交修改

        cu.close()
        db.close()



if __name__ == '__main__':

















































































































