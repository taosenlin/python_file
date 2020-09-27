# coding:utf8
# Time:2020-03-22 17:34
# Author:TSL

import socket

sk = socket.socket()
sk.connect(("127.0.0.1", 13003))
print("客户端启动了")

while True:
    # 向女神发送数据
    inp ="追求者2:" + input(">>>")
    sk.sendall(inp.encode("utf8"))

    # 退出判断
    if inp == "exit": break

    # 接受消息
    server_data = sk.recv(1024)
    print(server_data.decode("utf8"))

sk.close()