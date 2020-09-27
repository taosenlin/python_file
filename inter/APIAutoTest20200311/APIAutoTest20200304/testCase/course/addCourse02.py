from lib.courseLib import add,list
import time
#新增一个系统中不存在的课程
from lib.loginLib import login
#0.用户登录
sessionid=login('auto','sdfsdfsdf')

#0.列出课程1
retDict0=list(1,500,sessionid)

#1.新增课程
courseName='初中化学'+ str(int(time.time()*10000))
retDict=add(courseName,'sdfdss',0,sessionid)
print(retDict)

if retDict['retcode']==0:
    print('>>>>>新增课程测试通过')
    id=retDict['id']

    #2.列出课程2
    retDict2=list(1,500,sessionid)
    if len(retDict0['retlist'])+1==len(retDict2['retlist']) :
        print('>>>>>列出课程测试通过')
    else:
        print('>>>>>>列出课程测试不通过')