# coding:utf8
# Time:2020-03-22 21:34
# Author:TSL

import socket

sk = socket.socket()
sk.bind(("127.0.0.1", 13000))
sk.listen()

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



while True:
    conn, addr = sk.accept()
    #接受客户端的表明身份
    client_name = conn.recv(1024).decode("utf8")
    print("客户端身份",client_name)
    conn.sendall(b"ok")


    while True:
        # 收消息
        client_data = conn.recv(1024).decode("utf8")
        print(client_data)

        if "exit" in client_data: break

        # 发消息
        server_data = input(">>>")
        conn.sendall(handleData(server_data).encode("utf8"))

    conn.close()