#coding : utf8
#Author : taosenlin
#Time : 2020/7/22 9:50

# 1、json.dumps是将一个python数据类型列表进行json格式的编码解析
"""
import json

ele = ['stuPython',[1,2,3],{'a':'b'}]
encode_json = json.dumps(ele)          #json格式的编码
print(encode_json)
print(type(encode_json))

这样我们就将一个list列表对象，进行了json格式的编码转换
"""



# 2、解码python json格式，可以用json模块的json.loads()函数的解析方法

import json

ele = ['stuPython',[1,2,3],{'a':'b'}]

encode_json = json.dumps(ele)           #json格式的编码（将list类型编码为str类型）
print(encode_json)
print(type(encode_json))

decode_json = json.loads(encode_json)   #json格式的解码（将str类型解码为list类型）
print(decode_json)
print(type(decode_json))











































