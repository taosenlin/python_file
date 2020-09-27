# coding:utf8
# Time:2020-03-19 20:56
# Author:TSL

import threading
import time

a = []

def foo():
    while True:
        a.append("1")
        print("生产了一个数据")

t1 = threading.Thread(target=foo)
# t2 = threading.Thread(target=foo)

# 设置守护线程，必须在 start 之前设置
# 其作用就是在主线程想要退出进程的时候，不需要等待自己(子线程)运行结束，直接退出就行了
# 只对设置了守护线程的线程生效
t1.setDaemon(True)

t1.start()
# t2.start()



for i in range(10):
    if a:
        a.remove("1")
        print("消费了一个数据")
    time.sleep(1)

print("不需要再消费数据了")




































































