# Time:2020-03-03 21:22
# Author:TSL

import requests

# # 1、百度首页
# url = "http://www.baidu.com"
# r = requests.get(url)
# r.encoding = 'utf-8'
# print(r.text)
#
#
# # 2、列出课程
# url = 'http://localhost/api/mgr/sq_mgr/'
# payload = {'action':'list_course','pagenum':1,'pagesize':20}
# r = requests.get(url,params=payload)
# # r.encoding = 'utf-8'
# print(r.text)
#
#
# 3、新增课程
# url = 'http://localhost/api/mgr/sq_mgr/'
# payload = {
#     'action':'add_course',
#     'data':"""{
#     "name":"初中化学",
#     "desc":"初中化学课程",
#     "display_idx":"4"
#     }
# """
# }
# r = requests.post(url,data=payload)
# print(r.json())
#
#
# # 4、新增课程2
# url = 'http://localhost/apijson/mgr/sq_mgr/'
# dict1 = {"Content-Type":"application/json"}
# payload = {
#   "action" : "add_course_json",
#   "data"   : {
#     "name":"初中化学2236",
#     "desc":"初中化学课程",
#     "display_idx":"4"
#   }
# }
# r = requests.post(url,json=payload,headers=dict1)
# r.encoding = 'utf-8'
# print(r.json())


# 5、用户登录
# url = 'http://localhost/api/mgr/loginReq'
# payload = {
#     "username":"auto",
#     "password":"sdfsdfsdf"
# }
# r = requests.post(url,data=payload)
# print(r.json())
# print(r.status_code)     #获取状态码
# print(r.headers)         #获取响应头
# print(r.cookies)         #获取cookies
# print(r.cookies['sessionid'])    #获取sessionid




































































