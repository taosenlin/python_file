#coding : utf8
#Author : taosenlin
#Time : 2020/3/19 11:56

# 一、正则表达式的概述 （一套规则，不限于语法或工具）
# 对于复杂、无规则的字符串进行操作（提取）

# 二、正则表达式的作用
# 1、主要是针对字符串进行操作，可以简化对字符串的复杂操作

### （1）匹配：检查字符串是否符合正则表达式中的规则
# （2）切割：按一定的规则将字符串分割成多个子字符串
# （3）替换：将字符串中符合规则的字符替换成指定字符
### （4）获取：获取与规格相符的字符串



# 三、实用语法

# 1、通配符 .
# 可以匹配任何除换行符 "\n" 外的字符

# 例：
# 待匹配文本："songqin"
# 正则表达式："s.....n"
# 匹配结果为："songqin"


# 2、（pattern）*
# 允许模式重复0次或多次

# 例：
# 待匹配文本："www.songqin.com"
# 正则表达式："w*\.songqin\.com"    #反斜杠转义，避免被认为是通配符
# 匹配结果为："www.songqin.com"


# 3、（pattern）+
# 允许模式重复1次或多次

# 例：
# 待匹配文本："www.songqin.com"
# 正则表达式："w+\.songqin\.com"    #反斜杠转义，避免被认为是通配符
# 匹配结果为："www.songqin.com"



# 四、实际应用
import re

# 1、.
# res = re.findall('1.3','abcd123,143')
# print(res)
# （正则表达式，被处理的数据）---返回是list
# ['123', '143']


# 2、*
# res = re.findall('1.*','abcd123,143')
# print(res)
# ['123,143']


# res = re.findall('ab*','abcdabddac')
# print(res)
# ['ab', 'ab', 'a']
# res = re.findall('ab+','abcdabddac')
# print(res)
# ['ab', 'ab']


# 3、?
# 匹配0个或者1个由前面的正则表达式定义的片段，非贪婪方式（?前面的表达式找到了，就停止）

# 例：
# 待匹配文本："songqin"
# 正则表达式："so(.+?)"
# 匹配结果为："songqin"


# 4、() 括号里面是需要查找的内容
# 匹配括号内的表达式，也表示一个组

# res = re.findall('(songqin)','songqinsongqin')
# print(res)
# ['songqin', 'songqin']

# 例：
# 待匹配文本："songqinsongqin"
# 正则表达式："(songqin){2}"
# 匹配结果为："songqinsongqin"



# 五、其他应用
# 模式         描述
# \w           匹配字母数字及下划线
# \W           匹配非字母数字及下划线
# \S           匹配任意非空字符
# \d           匹配任意数字，等价于[0-9]
# \D           匹配任意非数字
# ^            匹配字符串的开头
# $            匹配字符串的末尾


# 1、 \w   字母、数字、下划线
# res = re.findall('\w+','*#abc123_ABC')
# print(res)
# ['abc123_ABC']


# 2、 \W   匹配非字母、数字、下划线
# res = re.findall('\W+','*#abc123_ABC###')
# print(res)
# ['*#', '###']


# 3、 \S   匹配任意非空字符
# res = re.findall('\S+','*#abc 123_ABC ###')
# print(res)
# ['*#abc', '123_ABC', '###']


# 4、 \d   匹配任意数字，等价于[0-9]
# res = re.findall('\d+','abc18119955930ABC')
# print(res)
# ['18119955930']
# res = re.findall('\d{11}','abc18119955930ABC')   #前面表达式的{位数}
# print(res)
# ['18119955930']


# 5、 ^    匹配字符串的开头
# res = re.findall('^1\d{10}','18119955930ABC')
# print(res)
# ['18119955930']
# res = re.findall('^1\d{9}0$','18119955930')
# print(res)
# ['18119955930']

































