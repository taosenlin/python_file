# coding:utf8
# Time:2020-07-04 15:00
# Author:TSL

import requests

url = "http://localhost/api/mgr/sq_mgr/"
dict1 = {'Content-Type':'application/x-www-form-urlencoded'}
playload = {
    'action': 'delete_teacher',
    'id':4
}

res = requests.delete(url,headers=dict1,data=playload)
print(res.json())
