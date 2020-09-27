# coding:utf8
# Time:2020-03-22 15:03
# Author:TSL

import socket

#创建socket对象
sk = socket.socket()
#客户端不需要设置ip地址和端口号，ip地址就是设备的ip地址，端口号由系统分配一个空闲的端口号

#发起连接
sk.connect(("127.0.0.1",13000))

#发送消息
send_data = input(">>>")
#发送数据（到服务端）
sk.sendall(send_data.encode("utf8"))

#接受消息（接受服务端发来的消息）
server_data = sk.recv(1024).decode("utf8")
print("服务端:",server_data)

#释放资源
sk.close()





















































































