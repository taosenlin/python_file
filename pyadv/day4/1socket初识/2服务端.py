# coding:utf8
# Time:2020-03-22 15:03
# Author:TSL

import socket

#配置服务端的ip地址和端口号
ip = ("127.0.0.1",13000)

#创建socket对象
sk = socket.socket()

#绑定ip地址和端口号
sk.bind(ip)

#监听有没有请求过来
sk.listen()
print("服务端启动了")

#等待传入连接，连接成功之前，阻塞状态
#等到连接传入之后，会返回一个新的套接字对象（socket对象）和客户端的ip地址,端口号
conn,addr = sk.accept()   #俩个变量分别对应第一个返回的套接字对象和第二个返回的ip地址,端口号
print("客户端的ip地址是:",addr)

#接受消息
client_data = conn.recv(1024).decode("utf8")
print("客户端:",client_data)

#一串逻辑处理（忽略）

send_data = input(">>>")
#发送数据
conn.sendall(send_data.encode("utf8"))

#释放资源
conn.close()
sk.close()
















































































