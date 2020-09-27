# coding:utf8
# Time:2020-03-18 8:17
# Author:TSL

import requests

def login():
    def foo():
        url = "www.xxx.com"

        payload = {
            "user1":"123",
            "user2":"123",
        }

        re = requests.post(url,data=payload)
        # print(re.json())
        return re.json()['token']
    return foo


@login
def my_log():
    print('this is my_log')





































































































