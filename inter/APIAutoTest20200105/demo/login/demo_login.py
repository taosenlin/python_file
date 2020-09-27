#【案例5】：用户登录
from config import HOST
import requests

dict1={'Content-Type':'application/x-www-form-urlencoded'}
payload={
    "username":"auto",
    "password":"sdfsdfsdf"
}
r=requests.post(f'{HOST}/api/mgr/loginReq',headers=dict1,data=payload)

print(r.text)


