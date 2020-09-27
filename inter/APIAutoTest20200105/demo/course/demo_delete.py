import requests
from config import HOST

header={'Content-Type':'application/x-www-form-urlencoded'}

payload={'action':'delete_course','id':1883}

r=requests.delete(f'{HOST}/api/mgr/sq_mgr/',headers=header,data=payload)
print(r.text)
