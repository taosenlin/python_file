# coding:utf8
# Time:2020-07-04 14:59
# Author:TSL

import requests

url = "http://localhost/api/mgr/sq_mgr/"
dict1 = {'Content-Type':'application/x-www-form-urlencoded'}
playload = {
    'action':'add_teacher',
    'data':"""{
    "username":"taosenlin",
    "password":"sq888",
    "realname":"tsl",
    "desc":"陶森林老师",
    "courses":[{"id":1,"name":"大学数学"}],
    "display_idx":1
     }
    """
}

res = requests.post(url,headers=dict1,data=playload)
print(res.json())













































