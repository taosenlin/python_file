import requests
from config import HOST
header={'Content-Type':'application/x-www-form-urlencoded'}

payload={'action':'modify_course',
         'id':'1885',
        'newdata':'''{
                  "name":"初中化学8888",
                  "desc":"初中化学课程",
                  "display_idx":"4"
                }'''
         }

r=requests.put(f'{HOST}/api/mgr/sq_mgr/',headers=header,data=payload)
print(r.text)