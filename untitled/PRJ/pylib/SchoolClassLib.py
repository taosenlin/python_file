# coding:utf8
# Time:2020-07-12 21:03
# Author:TSL

from cfg import g_vcode
import requests
from pprint import pprint
from robot.libraries.BuiltIn import BuiltIn       #设置全局变量

class SchoolClassLib:

    url = "http://ci.ytesting.com/api/3school/school_classes"

    def __init__(self):
        self.vcode = g_vcode

    def list_school_class(self,gradeid=None):
        if gradeid == None:
            payload = {
                'vcode':self.vcode,
                'action':'list_classes_by_schoolgrade'
            }
        else:
            payload = {
                'vcode':self.vcode,
                'action':'list_classes_by_schoolgrade',
                'gradeid':int(gradeid)
            }

        res = requests.get(self.url,params=payload)
        bodyDict = res.json()
        pprint(bodyDict,indent=2)
        return bodyDict



    def add_school_class(self,grade,name,studentlimit,isSaveId=None):
        payload = {
            'vcode':self.vcode,
            'action':'add',
            'grade':grade,
            'name':name,
            'studentlimit':studentlimit
        }
        res = requests.post(self.url,data=payload)
        bodyDict = res.json()

        #设置isSaveId为全局变量
        if isSaveId:
            BuiltIn().set_global_variable("${%s}"%isSaveId,bodyDict["id"])

        pprint(bodyDict,indent=2)
        return bodyDict




    def modify_school_class(self,classid,name,studentlimit):
        url = f'{self.url}/{classid}'
        payload = {
            'vcode':self.vcode,
            'action':'modify',
            'name':name,
            'studentlimit':studentlimit
        }
        res = requests.put(url,data=payload)
        bodyDict = res.json()
        pprint(bodyDict,indent=2)
        return bodyDict



    def delete_school_class(self,classid):
        url = f'{self.url}/{classid}'
        payload = {
            'vcode':self.vcode
        }
        res = requests.delete(url,data=payload)
        bodyDict = res.json()
        pprint(bodyDict,indent=2)
        return bodyDict



    def delete_all_school_class(self):

        #列出课程
        rd = self.list_school_class()
        # pprint(rd,indent=2)

        #删除课程
        for i in rd['retlist']:
            self.delete_school_class(i['id'])

        #再次列出课程
        rd = self.list_school_class()
        # pprint(rd,indent=2)

        if rd['retlist'] != []:
            raise Exception("can not delete all school class!")



    def classlist_should_contain(self,
                                 classlist,
                                 classname,
                                 gradename,
                                 invitecode,
                                 studentlimit,
                                 studentnumber,
                                 classid,
                                 expectedtimes=1
                                        ):
        item = {
            "name":classname,
            "grade__name":gradename,
            "invitecode": invitecode,
            "studentlimit": int(studentlimit),
            "studentnumber": int(studentnumber),
            "id": classid,
            "teacherlist": []
        }

        # if item not in classlist:
        #     raise Exception('班级列表里没有该班级')
        outtimes = classlist.count(item)
        if outtimes != expectedtimes:
            raise Exception(f'班级列表中该班级期望出现{expectedtimes}次，实际出现{outtimes}次！')


if __name__ == '__main__':
    a = SchoolClassLib()
    # a.add_school_class(1,'2班',60)
    a.list_school_class(1)
    # a.delete_school_class(444321)
