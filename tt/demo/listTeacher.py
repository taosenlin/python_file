# coding:utf8
# Time:2020-07-04 14:59
# Author:TSL

import requests

url = "http://localhost/api/mgr/sq_mgr/?action=list_teacher&pagenum=1&pagesize=20"
dict1 = {'Content-Type':'application/x-www-form-urlencoded'}

playload = {
    'action':'list_teacher',
    'pagenum': 1,
    'pagesize': 20
}
res = requests.get(url,headers=dict1,params=playload)
print(res.json())


