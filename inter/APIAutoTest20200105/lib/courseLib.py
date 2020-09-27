import requests
from config import HOST
import pprint

# 新增课程1
def add(name,desc,display_idx):
    dict1 = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {
        'action': 'add_course',
        'data': f'''{{"name":"{name}",
        "desc":"{desc}",
        "display_idx":{display_idx}}}
        '''
    }
    r = requests.post(f"{HOST}/api/mgr/sq_mgr/"
                      , headers=dict1, data=payload
                      )
    return r.json()

#2.列出课程
def list(pagenum,pagesize):
     payload = {"action": "list_course",
                "pagenum": pagenum,
                "pagesize": pagesize
                }
     r = requests.get(f'{HOST}/api/mgr/sq_mgr/', params=payload)
     return r.json()

#3. 删除课程
def delete(id):
    header = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'action': 'delete_course', 'id': id}
    r = requests.delete(f'{HOST}/api/mgr/sq_mgr/', headers=header, data=payload)
    return r.json()

#4.修改课程
def  modify(id,name,desc,display_idx):
    header = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'action': 'modify_course',
               'id': id,
               'newdata': f'''{{
                      "name":"{name}",
                      "desc":"{desc}",
                      "display_idx":"{display_idx}"
                    }}'''
               }

    r = requests.put(f'{HOST}/api/mgr/sq_mgr/', headers=header, data=payload)
    return r.json()
#5.新增课程2
def add2(name,desc,display_idx):
    dict1 = {'Content-Type': 'application/json'}
    payload = f'''
    {{
      "action" : "add_course_json",
      "data": {{
        "name":"{name}",
        "desc":"{desc}",
        "display_idx":"{display_idx}"
      }}
    }}
    '''
    r = requests.post(f'{HOST}/apijson/mgr/sq_mgr/', headers=dict1,
                      data=payload.encode(encoding='UTF-8'))

    return r.json()

