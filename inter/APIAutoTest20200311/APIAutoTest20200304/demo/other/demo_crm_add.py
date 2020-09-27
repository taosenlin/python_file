import requests
from demo.other.demo_token import getTokn
token=getTokn('fancl','sq000000')
# print(token)

header={
    'X-AUTH-TOKEN':token,
    'Content-Type':'application/json'
}
# data + 字符串
# json + 字典
payload={
    'aac003': '张三三',
    'aac004': '1',
    'aac011': '21',
    'aac030': '13575726388',
    'aac01u': '88002255',
    'crm003': '1',
    'crm004': '1',
    'crm00a': '2018-11-11',
    'crm00b': 'aaaaaa',
    'crm00c': '2019-02-28',
    'crm00d': 'bbbbbb'
}

r=requests.post('http://47.96.181.17:9090/rest/ac01CrmController',headers=header,
                json=payload)

print(r.json())


