# Time:2020-03-17 8:11
# Author:TSL

# 1
import os

#相当于打开操作系统的shell,并执行敲入的一串命令
# os.system("ipconfig")
'''
os.system("cmd.exe")    #当os.system中的代码执行完才会执行下面的print("after"),故称为阻塞式调用
print("after")
'''
# ret = os.system("ipconfi")
# print(ret)
# 0        返回值为0,说明调用成功
# 1        返回值为1,说明调用失败
# 返回值是程序的退出码



# 2
import subprocess

'''
#执行一个指定的命令,并将结果以一个字节字符串的形式返回
out = subprocess.check_output("ipconfig")
print(out.decode("gbk"))
'''
#check_output以一个返回值的形式返回(不直接打印出结果)
# out = subprocess.check_output("mspaint")    #画图板结束后才会打印print("after"),亦是阻塞式调用
# print("after")



# 3
#非阻塞式调用
from subprocess import Popen,PIPE

# (1)
'''
child = Popen("mspaint")
#Popen类中提供等待功能
# child.wait()

print(child)
'''

# (2)
# child = Popen("ipconfig")     #默认标准输出文件是屏幕
# child.wait()


# (3)
'''
#输出重定向
child = Popen(
     "ipconfig",
     stdout=PIPE,
     # stderr=PIPE,
     # encoding="gbk"
)

output,err = child.communicate()
print(output.decode("gbk"))
# errout = child.communicate()
# print(errout)
'''


# (4)
'''
# 输入重定向
child = Popen(
     "python ioTest.py",
     stdin=PIPE,
     stdout=PIPE,
     stderr=PIPE,
     encoding="gbk"
)
in_put,err = child.communicate("\n".join(["1","2"]))
print(in_put)
'''





































































