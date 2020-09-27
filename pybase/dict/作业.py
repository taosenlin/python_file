# Time:2020-02-16 20:26
# Author:TSL

fileDir = r'D:\0005_1.txt'
def putInfoToDict(fileName):
    resDict = {}       #定义字典
    with open(fileName) as fo:
        lines = fo.read().splitlines()         #获取所有行
        for line in lines:
            line = line.replace('\t','').replace('(','').replace(')','').replace("'",'').replace(';',',')  #处理多余的字符
            temp = line.split(',')
            checkTime = temp[0].strip()
            lessonId = int(temp[1].strip())
            userId = int(temp[2].strip())
            info = {'lessonid':lessonId,'checkintime':checkTime}  #统计信息---排版

            if userId not in resDict:            #如果开始不在字典---新增进去   键 = []
                resDict[userId] = [info]
            else:
                resDict[userId].append(info)
    return resDict

res = putInfoToDict(fileDir)
import pprint
pprint.pprint(res)

# pprint  完美打印---特别在接口响应数据上使用---模块使用前导入即可
































