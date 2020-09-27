# Time:2020-03-15 21:18
# Author:TSL

import unittest
import MySQLdb

class TestClass(unittest.TestCase):              #测试类

    @classmethod
    def setUpClass(cls):
        "连接数据库，做数据初始化操作"

        # 打开数据库连接
        db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="123456", port=3306, db="plesson", charset="utf8")

        # 获取操作游标
        cu = db.cursor()

        sql1 = """
        insert into sq_course(name,`desc`,display_idx)
        values
        """
        sql2 = ""
        for i in range(10):
            if i == 9:
                sql2 += """('sql课程{}','sql课程描述',1);""".format(i)
                break
            sql2 += """('sql课程{}','sql课程描述',1),""".format(i)
            sql2 += "\n"

        # print(sql2)
        sql = sql1 + sql2

        # 执行sql
        cu.execute(sql)  # 这个函数接收的参数为字符串
        # 涉及到数据库修改的都需要提交（增(insert)、删(delete)、改(update)）
        db.commit()
        print('插入成功')

        # 获取返回值
        # data = cu.fetchall()

        cu.close()
        db.close()
        # return data



    def testAdd(self):        #测试用例
        assert 1 == 1


    @classmethod
    def tearDownClass(cls):
        "连接数据库，做数据清理操作"

        # 打开数据库连接
        db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="123456", port=3306, db="plesson", charset="utf8")

        # 获取操作游标
        cu = db.cursor()

        #构造sql语句
        sql = """
        delete from sq_course
        where name like '%课程%';
        """
        cu.execute(sql)
        #提交数据库修改
        db.commit()
        print('删除成功')

        #释放资源
        cu.close()
        db.close()



if __name__ == '__main__':
    lo = unittest.TestLoader()   #测试加载器
    suite = unittest.TestSuite()   #创建测试组

    tests = lo.loadTestsFromTestCase(TestClass)    #从测试类加载测试用例

    #把测试用例加到测试组
    suite.addTests(tests)

    #运行测试组
    unittest.TextTestRunner(verbosity=2).run(suite)

















































































