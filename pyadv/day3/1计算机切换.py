# coding:utf8
# Time:2020-03-19 7:52
# Author:TSL

import threading
import time

def foo(something,num):
    for i in range(num):
        print("CPU正在:",something)
        time.sleep(1)


#创建线程实例，target指向任务函数,args为target指向的函数传参
t1 = threading.Thread(target=foo,args=["看电影",3])
t2 = threading.Thread(target=foo,args=["听音乐",5])


#启动线程
t1.start()
t2.start()




# 并发：逻辑上具备同时处理多个任务的能力
# 并行：物理上在同一时刻执行多个并发任务






































































































