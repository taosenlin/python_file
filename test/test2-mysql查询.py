# coding:utf8
# Time:2020-06-21 20:43
# Author:TSL

import MySQLdb
import requests

def get_course_from_api():
    res = requests.get("http://localhost/api/mgr/sq_mgr/?action=list_course&pagenum=1&pagesize=20")
    return res.json()['retlist']     #返回为字典格式

def get_course_from_db():
    db = MySQLdb.connect(host='192.168.3.14',user='root',password='123456',port=3306,db='plesson',charset='utf8')
    #获取数据库连接

    cu = db.cursor()
    #获取操作游标

    sql = 'select * from sq_course;'
    cu.execute(sql)
    #执行sql语句

    data = cu.fetchall()
    #获取返回值

    cu.close()
    db.close()

    return data
    #返回为元组格式


if __name__ == '__main__':
    dbData = get_course_from_db()
    for ele in dbData:
        print(list(ele))

    apiData = get_course_from_api()
    for ele1 in apiData:
        print(list(ele1.values()))





































































































