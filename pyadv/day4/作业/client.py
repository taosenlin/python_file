# coding:utf8
# Time:2020-03-22 21:34
# Author:TSL

import socket

sk = socket.socket()
sk.connect(("127.0.0.1",13000))


my_name = "nathniel"

def handleData(data):
    #先处理消息第二部分
    if data == "nathniel":
        data_type = "1"
    else:
        data_type = "2"

    #处理消息第一部分
    str_len = len(data) + 7
    if len(str(str_len)) < 4:
        data_len = "0"*(4 - len(str(str_len))) + str(str_len)
    else:
        data_len = str(str_len)

    return data_len+"|"+data_type+"|"+data

#先自报家门
sk.sendall(handleData(my_name).encode("utf8"))
#收消息
sk.recv(1024)


while True:
    #发送消息
    client_data = input(">>>")
    sk.sendall(handleData(client_data).encode("utf8"))

    if "exit" in client_data: break

    #收消息
    server_data = sk.recv(1024).decode("utf8")
    print("服务端:",server_data)

