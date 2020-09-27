# Time:2020-03-16 7:42
# Author:TSL

# 在Python3以后，字符串和bytes类型彻底分开了。字符串是以字符为单位进行处理的，bytes类型是以字节为单位处理的。
#
# bytes数据类型在所有的操作和使用甚至内置方法上和字符串数据类型基本一样，也是不可变的序列对象。


# 1-
# a = "abc"
# b = b'abc'
# b = b'落红不是无情物,化作春泥更护花'
#
# print(type(a))
# print(type(b))
# <class 'str'>
# <class 'bytes'>
# 此处默认ASCII码



# 2-
txt = "落红不是无情物,化作春泥更护花"
bTxt = txt.encode("utf8")           #encode将字符串转为bytes类型

print(type(txt))
print(type(bTxt))
print(bTxt)
# <class 'str'>
# <class 'bytes'>
# b'\xe8\x90\xbd\xe7\xba\xa2\xe4\xb8\x8d\xe6\x98\xaf\xe6\x97\xa0\xe6\x83\x85\xe7\x89\xa9,\xe5\x8c\x96\xe4\xbd\x9c\xe6\x98\xa5\xe6\xb3\xa5\xe6\x9b\xb4\xe6\x8a\xa4\xe8\x8a\xb1'


c = b'\xe8\x90\xbd\xe7\xba\xa2\xe4\xb8\x8d\xe6\x98\xaf\xe6\x97\xa0\xe6\x83\x85\xe7\x89\xa9,\xe5\x8c\x96\xe4\xbd\x9c\xe6\x98\xa5\xe6\xb3\xa5\xe6\x9b\xb4\xe6\x8a\xa4\xe8\x8a\xb1'

print(c.decode("utf8"))          #decode 将bytes类型转为字符串
# 落红不是无情物,化作春泥更护花


































































































