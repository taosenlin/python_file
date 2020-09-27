# coding=utf-8
import time


def log(self):

    with open('test.log', 'a+',encoding='utf-8') as f:
        f.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+':'+self+'\n')
