# coding:utf8
# Time:2020-03-22 16:56
# Author:TSL

import socketserver

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        print("有人和女神搭讪了...")

        while True:
            #接受数据
            client_data = self.request.recv(1024).decode("utf8")   #相当于conn.recv()
            print(client_data)

            #退出判断
            if client_data == "exit":break

            #处理并发数据
            inp = input(">>>")
            self.request.sendall(inp.encode("utf8"))


server = socketserver.ThreadingTCPServer(("127.0.0.1",13003),MyServer)
print("女神上线了...")
#启动服务
server.serve_forever()       #不间断运行
























































































