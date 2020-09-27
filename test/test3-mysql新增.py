# coding:utf8
# Time:2020-06-21 21:49
# Author:TSL

import MySQLdb

db = MySQLdb.connect(host='192.168.3.14',user='root',password='123456',port=3306,db='plesson',charset='utf8')
#创建数据库连接

cu = db.cursor()
#获取游标

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

sql = sql1 + sql2

cu.execute(sql)
#执行sql语句
db.commit()
#涉及到数据库的修改都要提交（增、删、改）

data = cu.fetchall()
#获取sql语句执行的返回值

cu.close()
db.close()














































































































