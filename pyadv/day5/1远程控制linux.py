# coding:utf8
# Time:2020-03-22 17:48
# Author:TSL

import paramiko

#创建ssh对象
ssh = paramiko.SSHClient()

#设置连接方式,没有密钥就自动添加
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)

#连接远程主机(ip地址，端口号，用户名，密码)
ssh.connect("192.168.3.8",22,"root","sdfsdf")

"""
#在远程主机执行命令
stdin,stdout,stderr = ssh.exec_command("cd Desktop;echo 'print(888)' > test.py")
#打印输出
print(stdout.read().decode("utf8"))
"""

#创建sftp对象
sftp = ssh.open_sftp()

"""
#将本地文件传送到远程服务器
#第一个参数是本地文件的路径，第二个参数为远程机器的路径
sftp.put("D:\PyCharm\pybase\py爬虫.py","/root/Desktop/py爬虫.py")
"""

#将远程文件下载到本地
#第一个参数为远程机器路径，第二个参数为本地路径
sftp.get("/root/Desktop/test.py","./test.py")


#释放资源
ssh.close()
























































































