#【案例3】：教管系统-新增课程
import requests
from config import HOST
dict1={'Content-Type':'application/x-www-form-urlencoded'}
payload={
    'action':'add_course',
    'data':"""{"name":"初中化学34",
    "desc":"初中化学课程",
    "display_idx":"4"}"""
}
print(payload)
r=requests.post(f"{HOST}/api/mgr/sq_mgr/"
                ,headers=dict1,data=payload
                )
print(r.text)


