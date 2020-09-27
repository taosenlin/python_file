# Time:2020-03-16 8:21
# Author:TSL

# 1-
#初始化一个空的数据
pngData = b''          #空的二进制文件

#二进制模式读
with open('./qqjt.png','rb') as f:
    pngData = f.read()


# 二进制模式写
with open('./qqjt2.png','wb') as f:
    f.write(pngData)



# 注:
# 字典与json的区别?

# 字典是python的数据类型,json不是python的数据类型(是一种数据交换格式)

# json在python中 本质上是字符串,只不过按照 key:value 这种格式来的字符串
























































































