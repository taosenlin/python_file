# coding:utf8
# Time:2020-03-22 15:51
# Author:TSL

import socket

#创建socket对象
sk = socket.socket()
#绑定ip地址与端口号
sk.bind(("0.0.0.0",13001))
#监听
sk.listen()

def get_file(sk_obj):
    """
    接受文件的函数
    :param sk_obj:
    :return:
    """
    #接受文件大小
    file_size = int(sk_obj.recv(1024).decode("utf8"))#接收到的为bytes类型，需要解码为str,然后再转换为int类型

    #避免粘包
    sk_obj.sendall(b"ok")

    #接受文件名称
    file_name = sk_obj.recv(1024).decode("utf8")

    # 避免粘包
    sk_obj.sendall(b"ok")

    #接受文件内容
    with open("./%s" % file_name,"wb") as f:
        while file_size > 0:
            f.write(sk_obj.recv(1024))
            file_size = file_size - 1024

#等待客户端连接
conn,addr = sk.accept()

get_file(conn)

#释放资源
conn.close()  #公司真实环境一般也会关闭
sk.close()  #公司真实环境一般不关闭





































































