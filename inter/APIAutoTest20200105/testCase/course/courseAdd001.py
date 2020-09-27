from lib.courseLib import add,list


# 方法1：新增课程前列出课程  数量为N   新增后，数量变为N+1

#1 列出课程
retDict0=list(1,500)
print(retDict0)
#2.新增课程
retDict1=add('大学英语2','aaaa','1')
print(retDict1)
if retDict1['retcode']==0 :
    print('测试通过')
#3.再次列出课程
retDict2=list(1,500)
#4. 比较列出课程多了一门课程
if len(retDict0['retlist'])==len(retDict2['retlist'])-1 :
    print('测试通过!!!')


# 方法2:新增课程（返回ID）、列出课程,循环查看ID是否存在

