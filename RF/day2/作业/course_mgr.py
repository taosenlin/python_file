# coding:utf8
# Time:2020-03-25 22:43
# Author:TSL

import requests
from config import HOST
from login import loginLib

sessionid = loginLib('auto','sdfsdfsdf')

def listCourse(pagenum,pagesize):

    url = f"{HOST}/api/mgr/sq_mgr/"

    header = {"Content-Type":"application/x-www-form-urlencoded"}

    payload = {
        "action":"list_course",
        "pagenum":pagenum,
        "pagesize":pagesize
    }
    cookie = {"sessionid":sessionid}

    r = requests.get(url,params=payload,headers=header,cookies=cookie)
    # print(r.json()['retlist'])
    courseList = []
    for i in r.json()['retlist']:
        coursename = i['name']
        courseList.append(coursename)
    return courseList


if __name__ == '__main__':
    print(listCourse(1,20))