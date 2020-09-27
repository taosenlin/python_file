# Time:2020-03-15 17:23
# Author:TSL

import MySQLdb

# def get_course_from_db():
#打开数据库连接
db = MySQLdb.connect(host="127.0.0.1",user="root",passwd="123456",port=3306,db="plesson",charset="utf8")

#获取操作游标
cu = db.cursor()

#构造sql语句
# 1-
"""
sql = '''
insert into sq_course
VALUES(5,'大学英语1','大学英语','1')
'''
"""
# 2-
#一次性插入多条数据           #desc为sql中的关键字
# 方法一
"""
sql = '''
insert into sq_course(name,`desc`,display_idx)    
values('sql课程1','sql课程描述',1),
      ('sql课程2','sql课程描述',1),
      ('sql课程3','sql课程描述',1);
'''
"""

# 方法二
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
# print(sql)


#3-数据库中操作
'''
insert into sq_course(name,`desc`,display_idx)
select 'sql课程6','sql课程1描述',1 union
select 'sql课程7','sql课程1描述',1 union
select 'sql课程8','sql课程1描述',1;
'''
# 4-数据库中操作(从sq_km表中查数据插入sq_course)
'''
insert into sq_course(name,`desc`,display_idx)
select name,`desc`,display_idx sq_km;
'''



#执行sql
cu.execute(sql)    #这个函数接收的参数为字符串
#涉及到数据库修改的都需要提交（增(insert)、删(delete)、改(update)）
db.commit()

#获取返回值
data = cu.fetchall()

cu.close()
db.close()
# return data            #返回为元组格式
# print(data)
