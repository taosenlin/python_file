#Author : taosenlin
#Time : 2020/3/3 15:16

# 一、while循环
# 1、while循环语法
# while 条件表达式：
#     循环代码

# 2、条件表达式结果为True的时候，代码会一直循环执行

# 3、直到条件表达式结果为False



# def get_sum(start,end,step):
#     datasum = 0
#     cnt = start
#     while cnt <= end:
#         datasum += cnt
#         cnt += step
#     return datasum

# res = get_sum(1,10,2)
# print(res)


# 例：请打印出1到100所有数字
# cur = 1
# while cur <= 100:
#     print(cur)
#     cur += 1
# 注意点：初始值、条件表达式、循环体内计数变量的增加



# 4、死循环（有些死循环是正常的，shell、GUI消息处理循环）
# while True:
#     print('press ctrl+c to exit')

#while True: ---不确定循环次数，循环靠条件结束时可以写

# while True:
#     password = input('请输入密码:')
#     if password == '123':
#         break   #结束循环



# namelist = ['mike','jack','marry']
# idx = 0
# while idx < len(namelist):
#     print(namelist[idx])
#     idx += 1
# mike
# jack
# marry

# namelist = ['mike','jack','marry']
# for name in namelist:
#     print(name)
# mike
# jack
# marry
#for循环的遍历--挨个取值（可迭代类型均可用）for循环（list、Tuple、str等）






# 二、for循环
# for i in range(1,10):
#     print(i)
#range范围左含右不含  （开始（可不写，默认0），结束，步调（可不写，默认1））



# while循环和for循环使用场景
# 已知循环次数或遍历操作用for循环
# 不确定次数，靠某个条件结束循环（while True:  if break）用while循环






# 三、break语句、continue语句
# namelist = ['mike','jack','tom']
# for name in namelist:
#     if name == 'jack':
#         # break      #结束循环
#         continue     #继续---结束本次循环，开始下次循环
#     print(name)
# print('run over')



'''
三个单引号敲回车（为自己定义的函数说明）
'''

#函数调用者--需要查询你的函数说明    函数名.__doc__
# print(print.__doc__)




























































































