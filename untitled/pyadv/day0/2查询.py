# Time:2020-03-15 12:30
# Author:TSL

import requests
import MySQLdb


def get_course_from_api():
    res = requests.get("http://localhost/api/mgr/sq_mgr/?action=list_course&pagenum=1&pagesize=20")

    return res.json()['retlist']          #返回为字典格式


def get_course_from_db():
    #打开数据库连接
    db = MySQLdb.connect(host="127.0.0.1",user="root",passwd="123456",port=3306,db="plesson",charset="utf8")

    #获取操作游标
    cu = db.cursor()

    #构造sql语句
    sql = '''
    select * 
    from sq_course;
    '''
    #执行sql
    cu.execute(sql)    #这个函数接收的参数为字符串
    #获取返回值
    data = cu.fetchall()

    cu.close()
    db.close()
    return data            #返回为元组格式


if __name__ == '__main__':
    dbData = get_course_from_db()
    apiData = get_course_from_api()

    for ele in dbData:
        print(list(ele))
    for ele1 in apiData:
        print(list(ele1.values()))



































































