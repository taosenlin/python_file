# coding:utf8
# Time:2020-03-19 22:19
# Author:TSL

import threading
import time

lockA = threading.Lock()      #面试官的锁
lockB = threading.Lock()      #小明的锁


#面试官
def foo1():
    lockA.acquire()   #上锁
    print("请解释什么是死锁")
    time.sleep(1)

    lockB.acquire()   #上锁
    print("发 offer")
    time.sleep(1)

    lockA.release()   #释放锁
    lockB.release()   #释放锁

#小明
def foo2():
    lockB.acquire()  # 上锁
    print("发 offer")
    time.sleep(1)

    lockA.acquire()  # 上锁
    print("请解释什么是死锁")
    time.sleep(1)

    lockA.release()   #释放锁
    lockB.release()   #释放锁

t1 = threading.Thread(target=foo1)
t2 = threading.Thread(target=foo2)

t1.start()
t2.start()
