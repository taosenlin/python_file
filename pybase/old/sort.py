# Time:2020-01-09 21:41
# Author:TSL
# 请定义一个函数 mySort，参数为一个列表，参数列表中的元素都是整数.
# mySort 函数需要将参数列表中的元素按从小到大排序，最终返回一个新的list。
#
# 请按下面算法的思路实现函数：
#
# 1. 创建一个新的列表newList
# 2. 先找出所有元素中最小的，append在newList里面
# 3. 再找出剩余的所有元素中最小的，append在newList里面
# 4. 依次类推，直到所有的元素都放到newList里面


newList = []                         #创建一个新的列表
def mySort(aList):
    for i in range(len(aList)):
        number = min(aList)             #找出所有元素中最小的元素
        newList.append(number)           #将找到的最小元素添加到新的列表中
        aList.remove(number)            #删除mySort列表中已经找到的最小元素，避免重复被找
    return newList

print(mySort([3, 5, 7, 2]))

