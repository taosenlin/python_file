#Author : taosenlin
#Time : 2020/3/2 15:14

# 一、对象方法概念
# 1、python中的一切类型的数据都是对象：数据和方法
# 2、对象：数据和方法
# 3、对象方法：
# （1）可以看做对象的行为
# （2）对象方法其实就是属于该对象的函数
# （3）可以以Obj.method(arg1,arg2,....)这样方式出现
# （4）相比函数func(arg1,arg2,....)
# 比如：    '12345'.find('123')
#            a = '12345'
#            a.find('123')



# 二、字符串方法
# 1、count  计算字符串包含的多少个指定的子字符串
# msg = '123 123 789'.count('123')
# print(msg)        #2

# str1 = 'abcdaaa'
# print(str1.count('a'))    #4   #直接调用为函数  加.为调用方法
# print(str1.__len__())     #7   #加__表示私有的或内部的方法



# 2、endswith 检查字符串是否以指定的字符串结尾
# 3、startswith 检查字符串是否以指定的字符串开头
# （返回是bool类型）
# msg = '139 123 789'.endswith('89')
# print(msg)          #True

# msg = '139 123 789'.startswith('13')
# print(msg)            #True



# 4、find
# (1)返回指定的子字符串在字符串中出现的位置
# msg = '123456789'.find('456')
# print(msg)                     #3

# (2)如果有多个，返回第一个(下标)，还可以指明从什么位置开始查找
#如果元素不存在，返回是-1
# msg = 'ok,good,name'.find(',')
# print(msg)                       #2

# msg = 'ok,good,name'.find(',',3)
# print(msg)                       #7


#    isspace  检查字符串是否只由空格组成
# 5、isalpha  检查字符串中是否都是字母
# 6、isdigit  检查字符串中是否都是数字
#返回是bool类型

# msg = 'abc1'.isalpha()
# print(msg)              #False

# msg = '123123'.isdigit()
# print(msg)                #True



# 7、str.join 将sequence类型的参数的元素字符串合并（连接）到一个字符串，string作为分隔符
# join (拼接) 定制化拼接，指定拼接符
# msg = ';'.join(['i','like','play','football'])
# print(msg)            #i;like;play;football



# 8、split将字符串分割为几个子字符串；参数为分隔符
#返回结果存放在一个list对象里（切割完为列表，切点会被切掉）

# str1 = 'abadea'
# print(str1.split('a'))    #['', 'b', 'de', '']   #返回是列表



# 9、lower  将字符串里面如果有大写字母的全部转为小写字母
# 10、upper 将字符串里面如果有小写字母的全部转为大写字母

# msg = 'China'.lower()
# print(msg)             #china

# msg = 'china'.upper()
# print(msg)               #CHINA



# 11、replace 替换字符串里面指定的子字符串
# str1 = 'name is tom tom'
# print(str1.replace('tom','jack'))
# name is jack jack     默认全部替换
# print(str1.replace('tom','jack',1))
#加位数表示替换几位（一依次替换）

# msg = 'name is tom'
# print(msg.replace(' ',''))
#nameistom



# 12、strip 将字符串前置空格和后置空格删除
# msg = '   good   '.strip()
# print(msg)                   #good

# 13、lstrip 将字符串前置空格删除
# msg = '  good  '.lstrip()
# print(msg)                     #good

# 14、rstrip 将字符串后置空格删除
# msg = '  good  '.rstrip()
# print(msg)                       #  good





































