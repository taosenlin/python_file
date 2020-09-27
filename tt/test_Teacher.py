# coding:utf8
# Time:2020-07-04 20:07
# Author:TSL

from lib.teacherLib import add_Teacher
from lib.teacherLib import list_Teacher
import time

class Test_Teach():
    def test_Teach(self):
        #新增一个老师
        username = 'tt' + str(int(time.time()*10000))
        retDict = add_Teacher(username,'sq888','tsl','smart',1,1,'大学数学')
        print(retDict)

        if retDict['retcode'] == 0:
            id = retDict['id']

            #列出老师
            retDict2 = list_Teacher(1,20)
            # print(retDict2)
            ret = retDict2['retlist'][-1]
            print("新增老师的信息:",ret)
            if ret['id'] == id:
                print(">>>>>>>>测试通过<<<<<<<<")
            else:
                print(">>>>>>>>测试不通过<<<<<<")

# test_Teach()

































