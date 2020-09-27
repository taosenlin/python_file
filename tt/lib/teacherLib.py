# coding:utf8
# Time:2020-07-04 16:45
# Author:TSL

import requests

#1-新增老师
def add_Teacher(username,password,realname,desc,display_idx,id,name):
    url = "http://localhost/api/mgr/sq_mgr/"
    dict1 = {'Content-Type':'application/x-www-form-urlencoded'}
    playload = {
        'action':'add_teacher',
        'data':f"""{{
        "username":"{username}",
        "password":"{password}",
        "realname":"{realname}",
        "desc":"{desc}",
        "courses":[{{"id":"{id}","name":"{name}"}}],
        "display_idx":"{display_idx}"
         }}
        """
    }
    try:
        res = requests.post(url,headers=dict1,data=playload)
        return res.json()
    except:
        return {'retcode': '0001', 'reason': '增加老师异常'}

# add1 = add_Teacher('wulan1','sq888','wl','beautiful',1,2,'大学语文')
# print(add1)


#2-列出老师

def list_Teacher(pagenum,pagesize):
    url = "http://localhost/api/mgr/sq_mgr/?action=list_teacher&pagenum=1&pagesize=20"
    dict1 = {'Content-Type':'application/x-www-form-urlencoded'}

    playload = {
        'action':'list_teacher',
        'pagenum': pagenum,
        'pagesize': pagesize
    }
    try:
        res = requests.get(url,headers=dict1,params=playload)
        return res.json()
    except:
        return {'retcode': '0002', 'reason': '列出老师异常'}

# print(list_Teacher(1,20))


#3-删除老师
def delete_Teacher(id):
    url = "http://localhost/api/mgr/sq_mgr/"
    dict1 = {'Content-Type':'application/x-www-form-urlencoded'}
    playload = {
        'action': 'delete_teacher',
        'id':id
    }
    try:
        res = requests.delete(url,headers=dict1,data=playload)
        return res.json()
    except:
        return {'retcode':'0003','reason':'删除老师异常'}

# print(delete_Teacher(7))








