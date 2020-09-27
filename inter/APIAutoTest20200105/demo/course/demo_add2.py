#【案例4】：教管系统-新增课程2
import requests
from config import HOST
dict1={'Content-Type':'application/json'}
payload='''
{
  "action" : "add_course_json",
  "data": {
    "name":"初中化学442",
    "desc":"初中化学课程",
    "display_idx":"4"
  }
}
'''
r=requests.post(f'{HOST}/apijson/mgr/sq_mgr/',headers=dict1,
                data=payload.encode(encoding='UTF-8'))

print(r.text)