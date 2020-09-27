# coding:utf8
# Time:2020-03-22 22:17
# Author:TSL

# 0015|1|nickname

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

if __name__ == '__main__':
    print(handleData("888"))