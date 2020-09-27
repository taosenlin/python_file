# coding:utf8
# Time:2020-03-19 20:51
# Author:TSL

import threading
import time

def foo():
    time.sleep(3)
    print("888")

t1 = threading.Thread(target=foo)
t1.start()
t1.join()    #在线程t1结束运行之前，阻塞住主线程，不让继续往下运行


print("主线程最后一行代码")






































































