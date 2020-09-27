from lib.courseLib import add,list

# 方法2:新增课程（返回ID）、列出课程,循环查看ID是否存在
#1.新增课程
retDict1=add('大学英语5','aaaa','1')
print(retDict1)
if retDict1['retcode']==0 :
    print('测试通过')
    courseID=retDict1['id']
    #2.再次列出课程
    retDict2=list(1,500)
    #3. 循环查看新增课程的ID是否存在
    for item in retDict2['retlist'] :
        if item['id']==courseID :
            print('测试通过！！！ID号在列表中的确存在！！')
            break


