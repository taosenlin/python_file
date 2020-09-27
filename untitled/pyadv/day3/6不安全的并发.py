# coding:utf8
# Time:2020-03-19 21:40
# Author:TSL

import threading
import time


balance = 500            #银行卡账户余额
r = threading.Lock()     #声明一把锁

"""
这把锁是同步锁
同步锁必须 上锁与解锁 相对
否则会产生bug

如果上锁之后，不解锁，再次上锁，代码会阻塞
如果解锁之后，没有锁的时候，又进行解锁，代码会报错
"""

# 操作账户余额
def foo(num):

    #1、申明全局变量(局部修改全局变量的时候，必须要去声明)
    global balance

    """
    有一大段操作不涉及，这部分不需要锁的
    """
    r.acquire()      #上锁     锁在什么时候锁？---在所有涉及全局变量的操作之前锁

    #2、将变量存到自己的系统
    account_balance = balance

    time.sleep(2)   #防止代码太少，cpu执行速度太快，t1和t2变成串行

    #3、进行了一系列操作之后，计算出了结果
    account_balance = account_balance + num

    #4、将计算结果传递回去
    balance = account_balance

    r.release()      #解锁

# 消费300
t1 = threading.Thread(target=foo,args=(-300,))
# 收入了10000
t2 = threading.Thread(target=foo,args=(10000,))

# 启动线程
t1.start()
t2.start()

# 阻塞主线程
t1.join()
t2.join()


print("所有线程运行结束后，余额为:",balance)































































































