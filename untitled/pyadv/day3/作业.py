# coding:utf8
# Time:2020-03-22 21:15
# Author:TSL

import requests,threading

newStr = ""

def foo(url):
    global newStr
    re = requests.get(url)
    newStr += re.text

t1 = threading.Thread(target=foo,args=["http://mirrors.163.com/centos/6/isos/x86_64/README.txt"])
t2 = threading.Thread(target=foo,args=["http://mirrors.163.com/centos/7/isos/x86_64/0_README.txt"])

t1.start()
t2.start()

t1.join()
t2.join()

with open("./readme89.TXT","w",encoding="utf8") as f:
    f.write(newStr)

































































