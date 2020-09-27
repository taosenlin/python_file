#Author : taosenlin
#Time : 2020/3/9 11:43

# 一、循环嵌套
# girls = ['wu','ruan','wang']
# boys = ['huang','zhang','wang']
# for girl in girls:
#     for boy in boys:
#         print(girl,boy)

#九九乘法表
# for i in range(1,10):        #行
#     for j in range(1,i+1):   #列
#         print('{}*{}={}'.format(j,i,j*i),end=' ')
#     print('\n')
# (1)用途：列出所有的可能性组合
# (2)先从外层循环里面取出一个元素，再执行内层循环
# (3)当内层循环都执行完后，再继续执行外层循环



# 二、列表生成式
# 1、员工税前工资列表
# [10000,15000,8000,4000,5000]
# 每个员工扣税10%
# 计算出所有员工的税后工资，存储在列表中
# beforeTax = [10000,15000,8000,4000,5000]
# afterTax = []
# for i in beforeTax:
#     afterTax.append(i*0.9)
# print(afterTax)
# [9000.0, 13500.0, 7200.0, 3600.0, 4500.0]


# 2、典型的从源列表生成目标列表的处理方式
# (1)从源列表里面，一次取出元素
# (2)做同样的处理
# (3)放入另一个列表中
# beforeTax = [10000,15000,8000,4000,5000]
# afterTax = [int(one*0.9) for one in beforeTax]
# print(afterTax)
# [9000, 13500, 7200, 3600, 4500]

# afterTax = [int(one*0.9) for one in beforeTax if one >= 8000]
# print(afterTax)
# [9000, 13500, 7200]



# 三、排序算法
# 1、冒泡排序算法
# alist = [9,2,0,1,5]
# alist.sort()          #顺序
# print(alist)
# [0, 1, 2, 5, 9]
# print(alist[::-1])    #倒序（方法一）（先顺序排完才行）
# alist.reverse()       #倒序（方法二）
# print(alist)
# alist.sort(reverse=True)   #倒序
# print(alist)
# [9, 5, 2, 1, 0]
# alist.sort(reverse=False)    #顺序（升序）
# print(alist)
# [0, 1, 2, 5, 9]


# 2、代码实现冒泡排序
# 核心思路：[8,2,6,0]
# (1)每一次找一个较大值
# (2)相邻元素比较

# alist = [8,2,6,0]
#第一层循环---找几次较大值
# for i in range(1,len(alist)):      #1、2、3---3次
      #每一次较大值怎么找---俩俩对比，大的往后移
#     for j in range(0,len(alist)-i):
          #是否需要交换
#         if alist[j] > alist[j+1]:
#             alist[j],alist[j+1] = alist[j+1],alist[j]
# print(alist)














































