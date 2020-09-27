# coding:utf8
# Time:2020-03-19 8:05
# Author:TSL

import threading
import time

def foo(something):
    print(something)
    time.sleep(2)

begin_time = time.time()


#并发的成绩：总计消耗时长: 2.0015993118286133
#创建线程实例
t1 = threading.Thread(target=foo,args=("磁盘写入100兆数据",))
t2 = threading.Thread(target=foo,args=("cpu去做其他事情",))


#启动线程
t1.start()
t2.start()


#阻塞住主线程
t1.join()        #在线程 t1 运行结束之前，阻止主线程继续运行
t2.join()        #在线程 t2 运行结束之前，阻止主线程继续运行



'''
#串行成绩：总计消耗时长: 4.000492334365845
foo("磁盘写入100兆数据")
foo("cpu去做其他事情")
'''


end_time = time.time()
print("总计消耗时长:",end_time - begin_time)




























































































