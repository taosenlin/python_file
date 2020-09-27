# coding:utf8
# Time:2020-03-25 23:05
# Author:TSL

import requests
from config import HOST

def loginLib(username,password):
    url = f"{HOST}/api/mgr/loginReq"

    payload = {
        "username":username,
        "password":password
    }

    header = {"Content-Type":"application/x-www-form-urlencoded"}
    try:
        r = requests.post(url,data=payload,headers=header,verify=False)
        return r.cookies['sessionid']
    except:
        return {'retcode': '0001', 'reson': '程序异常'}