# Time:2020-03-17 7:20
# Author:TSL

import chardet

#获取文件编码类型
def get_encoding(file):
    #以二进制方式读取,获取字节数据,检测类型
    with open(file,"rb") as f:
        data = f.read(1024)             #读取1024个字节
        return chardet.detect(data)

file_name = './a.txt'

encodingData = get_encoding(file_name)

print(encodingData)






























































































