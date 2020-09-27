# coding:utf8
# Time:2020-03-19 8:18
# Author:TSL

import threading
import time

def foo():
    num = 0
    for i in range(10000000):
        num = num + 1

begin_time = time.time()

# 并发的成绩：总计消耗时长: 0.7969088554382324
#创建线程实例
t1 = threading.Thread(target=foo)
t2 = threading.Thread(target=foo)
#启动线程
t1.start()
t2.start()

#阻塞住主线程
t1.join()        #在线程 t1 运行结束之前，阻止主线程继续运行
t2.join()        #在线程 t2 运行结束之前，阻止主线程继续运行


# 串行成绩:总计消耗时长: 0.8148565292358398(只有一个线程)
# foo()
# foo()


end_time = time.time()
print("总计消耗时长:",end_time - begin_time)



















































































