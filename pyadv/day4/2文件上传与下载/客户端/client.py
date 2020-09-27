# coding:utf8
# Time:2020-03-22 15:51
# Author:TSL

import socket
import os

#创建socket对象
sk = socket.socket()
#发起连接
sk.connect(("127.0.0.1",13001))

def post_file(sk_obj,file_path):
    """
    发送文件
    :param sk_obj: socket对象
    :param file_path: 文件路径
    :return:
    """
    #发送文件大小
    file_size = os.stat(file_path).st_size         #获取文件大小
    sk_obj.sendall(str(file_size).encode("utf8"))  #将int转为str，再将str转为bytes(int类型不能直接转为bytes类型)，然后发送出去

    #避免粘包(recv起到阻塞的作用)
    sk_obj.recv(1024)

    # D:\PyCharm\pyadv\day4\2
    # 文件上传与下载\客户端\    qqjt.png
    #发送文件名称
    file_name = os.path.split(file_path)[1]  #文件路径切割后0为文件路径，1为文件名称
    sk_obj.sendall(file_name.encode("utf8"))

    # 避免粘包(recv起到阻塞的作用)
    sk_obj.recv(1024)

    #发送文件内容
    with open(file_path,"rb") as f:
        while file_size > 0:
            sk_obj.sendall(f.read(1024))
            file_size = file_size -1024


post_file(sk,"./qqjt.png")

#释放资源
sk.close()














































































