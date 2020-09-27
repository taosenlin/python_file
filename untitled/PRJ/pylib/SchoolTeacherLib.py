#coding : utf8
#Author : taosenlin
#Time : 2020/7/21 11:15

import requests
from pprint import pprint
from cfg import *
from robot.libraries.BuiltIn import BuiltIn
import json


class SchoolTeacherLib:

    url = "http://ci.ytesting.com/api/3school/teachers"

    def __init__(self):
        self.vcode = g_vcode

    def list_school_teacher(self,subjectid=None):

        params = {
            'vcode': self.vcode,
            'action': 'search_with_pagenation'
        }
        if subjectid != None:
            params['subjectid'] = subjectid

        res = requests.get(self.url,params=params)
        bodyDict = res.json()
        pprint(bodyDict,indent=2)
        return bodyDict



    def add_school_teacher(self,username,realname,subjectid,classlist,
                           phonenumber,email,idcardnumber,isSaveId=None):
        tmplist = str(classlist)
        newClassList = [{"id":one.strip()} for one in tmplist.split(',') if one != '']

        payload = {
            'vcode':self.vcode,
            'action':'add',
            'username':username,
            'realname':realname,
            'subjectid':subjectid,
            'classlist':json.dumps(newClassList),
            'phonenumber':phonenumber,
            'email':email,
            'idcardnumber':idcardnumber
        }

        res = requests.post(self.url,data=payload)
        bodyDict = res.json()

        #设置isSaveId为全局变量
        if isSaveId != None:
            BuiltIn().set_global_variable("${%s}"% isSaveId,bodyDict["id"])

        pprint(bodyDict,indent=2)
        return bodyDict




    def modify_school_teacher(self,teacherid,realname=None,subjectid=None,
                              classlist=None,phonenumber=None,email=None,idcardnumber=None):
        payload = {
            'vcode': self.vcode,
            'action': 'modify',
        }

        # 230,231,232
        tmplist = str(classlist)
        newClassList = [{'id':one.strip()} for one in tmplist.split(',') if one != '']

        if realname != None:
            payload['realname'] = realname
        if subjectid != None:
            payload['subjectid'] = subjectid
        if classlist != None:
            payload['classlist'] = json.dumps(newClassList)
        if phonenumber != None:
            payload['phonenumber'] = phonenumber
        if email != None:
            payload['email'] = email
        if idcardnumber != None:
            payload['idcardnumber'] = idcardnumber

        url = f'{self.url}/{teacherid}'
        res = requests.put(url,data=payload)
        bodyDict = res.json()
        pprint(bodyDict,indent=2)
        return bodyDict




    def delete_school_teacher(self,teacherid):
        payload = {
            'vcode':self.vcode
        }
        url = f'{self.url}/{teacherid}'
        res = requests.delete(url,data=payload)
        bodyDict = res.json()
        pprint(bodyDict,indent=2)
        return bodyDict




    def delete_all_school_teacher(self):
        #列出课程
        rd = self.list_school_teacher()

        #删除课程
        for i in rd['retlist']:
            self.delete_school_teacher(i['id'])

        #再次列出课程
        rd = self.list_school_teacher()

        if rd['retlist'] != []:
            raise Exception("can not delete all school teacher!")




    def teacherlist_should_contain(self,
                                   teacherlist,
                                   username,
                                   realname,
                                   teacherid,
                                   classlist,
                                   phonenumber,
                                   email,
                                   idcardnumber,
                                   expectedtimes=1):

        teachclasslist = str(classlist)

        item = {
            'username':username,
            'realname':realname,
            'id':int(teacherid),
            'teachclasslist':[int(one.strip()) for one in
                              teachclasslist.split(',') if one != ''],
            'phonenumber':phonenumber,
            'email':email,
            'idcardnumber':idcardnumber
        }

        outtimes = teacherlist.count(item)
        if outtimes != expectedtimes:
            raise Exception("期望老师列表出现次数{},实际出现次数{}!".format(expectedtimes,outtimes))










if __name__ == '__main__':
    a = SchoolTeacherLib()
    # a.add_school_teacher('xiaotao','小陶',1,447120,15888668888,'tao@qq.com',210000000880000000)
    a.list_school_teacher()
    # a.modify_school_teacher(136275)
    # a.delete_school_teacher(135517)