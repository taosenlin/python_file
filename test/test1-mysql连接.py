# coding:utf8
# Time:2020-06-21 20:09
# Author:TSL

import MySQLdb

db = MySQLdb.connect(host='192.168.3.14',user='root',password='123456',port=3306,db='plesson')
#连接数据库

cu = db.cursor()
#获取操作游标

cu.execute('select version();')
#通过execute执行sql语句

data = cu.fetchone()
#获取sql语句执行结果（一行）
# data = cu.fetchall()
#获取所有行

print("数据库版本是:",data)

cu.close()
db.close()
#释放资源
















































































































