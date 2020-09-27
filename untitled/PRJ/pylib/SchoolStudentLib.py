#coding : utf8
#Author : taosenlin
#Time : 2020/7/21 16:49

import requests
from cfg import g_vcode
from pprint import pprint
from robot.libraries.BuiltIn import BuiltIn


class SchoolStudentLib:

    url = "http://ci.ytesting.com/api/3school/students"

    def __init__(self):
        self.vcode = g_vcode

    def list_school_student(self):
        payload = {
            'vcode':self.vcode,
            'action':'search_with_pagenation'
        }
        res = requests.get(self.url,params=payload)
        bodyDict = res.json()
        pprint(bodyDict,indent=2)
        return bodyDict



    def add_school_student(self,username,realname,gradeid,classid,phonenumber,
                           isSaveId=None):
        payload = {
            'vcode':self.vcode,
            'action':'add',
            'username':username,
            'realname':realname,
            'gradeid':gradeid,
            'classid':classid,
            'phonenumber':phonenumber
        }
        res = requests.post(self.url,data=payload)
        bodyDict = res.json()

        #设置isSaveId为全局变量
        if isSaveId != None:
            BuiltIn().set_global_variable("${%s}"% isSaveId,bodyDict["id"])

        pprint(bodyDict,indent=2)
        return bodyDict



    def modify_school_student(self,studentid,realname=None,phonenumber=None):
        payload = {
            'vcode':self.vcode,
            'action':'modify',
        }
        if realname != None:
            payload['realname'] = realname
        if phonenumber != None:
            payload['phonenumber'] = phonenumber

        url = f'{self.url}/{studentid}'
        res = requests.put(url,data=payload)
        bodyDict = res.json()
        pprint(bodyDict,indent=2)
        return bodyDict



    def delete_school_student(self,studentid):
        payload = {
            'vcode':self.vcode
        }
        url = f'{self.url}/{studentid}'
        res = requests.delete(url,data=payload)
        bodyDict = res.json()
        pprint(bodyDict,indent=2)
        return bodyDict



    def delete_all_school_student(self):

        #列出学生
        rd = self.list_school_student()
        ret = rd['retlist']

        #删除学生
        for i in ret:
            self.delete_school_student(i['id'])

        #再次列出学生
        rd = self.list_school_student()
        if rd['retlist'] != []:
            raise Exception("can not delete all school student!")




    def studentlist_should_contain(self,
                                   studentlist,
                                   classid,
                                   id,
                                   phonenumber,
                                   realname,
                                   username,
                                   expectedtimes=1):
        item = {
            'classid':classid,
            'id':id,
            'phonenumber':phonenumber,
            'realname':realname,
            'username':username
        }

        outtimes = studentlist.count(item)
        if outtimes != expectedtimes:
            raise Exception("期望出现此学生{}次,实际出现{}次!".format(expectedtimes,outtimes))










if __name__ == '__main__':
    a = SchoolStudentLib()
    a.list_school_student()
    # a.add_school_student('xiaozhang','小张',1,445339,15888888888)
    # a.modify_school_student(65807,'春野蓝')
    # a.delete_school_student(65897)