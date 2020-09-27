# Time:2020-03-15 17:37
# Author:TSL

import requests

data = [
    {"action":"add_course","data":'{"name":"课程01","desc":"01","display_idx":1}'},
    {"action":"add_course","data":'{"name":"课程02","desc":"02","display_idx":1}'},
    {"action":"add_course","data":'{"name":"课程03","desc":"03","display_idx":1}'},
    {"action":"add_course","data":'{"name":"课程04","desc":"04","display_idx":1}'},
    {"action":"add_course","data":'{"name":"课程05","desc":"05","display_idx":1}'},
    {"action":"add_course","data":'{"name":"课程06","desc":"06","display_idx":1}'},
]

#一行代码实现接口请求，一次性传100个数据

#1-方式一
# for i in data:
#     re = requests.post(url=r'http://localhost/api/mgr/sq_mgr/',data=i)
#     print(re.text)

##############################################

sli = []

for i in range(100):
    sli.append(i)


sli = [i for i in range(100)]

##############################################

#2-方式二
dataList = [requests.post(url=r'http://localhost/api/mgr/sq_mgr/',data=i) for i in data]

for res in dataList:
    print(res.text)


























































