# coding:utf8
# Time:2020-04-12 11:59
# Author:TSL

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from cfg import *
import time

class WebOpAdmin:
    #保证仅实例化一次
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def setupWebTest(self,driverType='chrome'):
        #self.driver保存WebDriver对象
        # self.driver = none
        if driverType == 'chrome':
            self.driver = webdriver.Chrome(r'D:\\ruanjiananzhuang\chromedriver.exe')
        else:
            raise Exception('unknow driver type %s' % driverType)

        self.driver.implicitly_wait(10)


    def tearDownWebTest(self):
        self.driver.quit()


    def loginWebSite(self):
        self.driver.get(LoginUrl)

        # self.driver.find_element_by_css_selector('[id="username"]').send_keys(adminuser['name'])
        # self.driver.find_element_by_css_selector('[id="password"]').send_keys(adminuser['pw'])
        self.driver.find_element_by_css_selector('[onclick="postLoginRequest()"]').click()


    def addCourse(self,name,desc,idx):
        #跳转到课程界面
        self.driver.find_element_by_css_selector('[ui-sref="course"]').click()
        #点击添加课程
        self.driver.find_element_by_css_selector('button[ng-click="showAddOne=true"]').click()
        #添加课名称
        s1 = self.driver.find_element_by_css_selector("input[ng-model='addData.name']")
        s1.clear()
        s1.send_keys(name)
        #详情描述
        s2 = self.driver.find_element_by_css_selector('textarea[ng-model="addData.desc"]')
        s2.clear()
        s2.send_keys(desc)
        #展示次序
        s3 = self.driver.find_element_by_css_selector('input[ng-model="addData.display_idx"]')
        s3.clear()
        s3.send_keys(idx)
        #创建课程
        self.driver.find_element_by_css_selector('button[ng-click="addOne()"]').click()
        time.sleep(1)


    def addTeacher(self,realname,username,desc,idx,lesson):
        # 跳转到老师界面
        self.driver.find_element_by_css_selector('[ui-sref="teacher"]').click()
        # 点击添加老师
        self.driver.find_element_by_css_selector('button[ng-click="showAddOne=true"]').click()
        # 添加老师姓名
        s1 = self.driver.find_element_by_css_selector('input[ng-model="addEditData.realname"]')
        s1.clear()
        s1.send_keys(realname)
        #添加登录名
        s2 = self.driver.find_element_by_css_selector('input[ng-model="addEditData.username"]')
        s2.clear()
        s2.send_keys(username)
        # 描述
        s3 = self.driver.find_element_by_css_selector('textarea[ng-model="addEditData.desc"]')
        s3.clear()
        s3.send_keys(desc)
        # 展示次序
        s4 = self.driver.find_element_by_css_selector('input[ng-model="addEditData.display_idx"]')
        s4.clear()
        s4.send_keys(idx)
        #授课信息
        s5 = Select(self.driver.find_element_by_css_selector('select[ng-model="$parent.courseSelected"]'))
        s5.select_by_visible_text(lesson)
        #点击加号按钮
        self.driver.find_element_by_css_selector('[ng-click="addEditData.addTeachCourse()"]').click()
        # 创建课程
        self.driver.find_element_by_css_selector('button[ng-click="addOne()"]').click()
        time.sleep(1)


    def addTrain(self,name,desc,idx,lesson1,lesson2):
        #跳转到培训班界面
        self.driver.find_element_by_css_selector('[ui-sref="training"]').click()
        # 点击添加培训班
        self.driver.find_element_by_css_selector('button[ng-click="showAddOne=true"]').click()
        # 添加培训班名
        s1 = self.driver.find_element_by_css_selector('[ng-model="addEditData.name"]')
        s1.clear()
        s1.send_keys(name)
        # 描述
        s2 = self.driver.find_element_by_css_selector('[ng-model="addEditData.desc"]')
        s2.clear()
        s2.send_keys(desc)
        # 展示次序
        s3 = self.driver.find_element_by_css_selector('[ng-model="addEditData.display_idx"]')
        s3.clear()
        s3.send_keys(idx)
        #包含课
        s4 = Select(self.driver.find_element_by_css_selector('[ng-model="$parent.courseSelected"]'))
        s4.select_by_visible_text(lesson1)
        #点击加号
        self.driver.find_element_by_css_selector('[ng-click="addEditData.addTeachCourse()"]').click()
        s5 = Select(self.driver.find_element_by_css_selector('[ng-model="$parent.courseSelected"]'))
        s5.select_by_visible_text(lesson2)
        # 点击加号
        self.driver.find_element_by_css_selector('[ng-click="addEditData.addTeachCourse()"]').click()
        # 创建培训班
        self.driver.find_element_by_css_selector('button[ng-click="addOne()"]').click()
        time.sleep(1)


    def trainGrade(self,name,desc,idx,lesson):
        # 跳转到培训班期界面
        self.driver.find_element_by_css_selector('[ui-sref="traininggrade"]').click()
        # 点击创建培训班期
        self.driver.find_element_by_css_selector('button[ng-click="showAddOne=true"]').click()
        # 添加班期
        s1 = self.driver.find_element_by_css_selector('input[ng-model="addEditData.name"]')
        s1.clear()
        s1.send_keys(name)
        # 描述
        s2 = self.driver.find_element_by_css_selector('textarea[ng-model="addEditData.desc"]')
        s2.clear()
        s2.send_keys(desc)
        # 展示次序
        s3 = self.driver.find_element_by_css_selector('input[ng-model="addEditData.display_idx"]')
        s3.clear()
        s3.send_keys(idx)
        #所属培训班
        s4 = Select(self.driver.find_element_by_css_selector('[ng-model="$parent.addEditData.training_id"]'))
        s4.select_by_visible_text(lesson)
        # 创建课程
        self.driver.find_element_by_css_selector('button[ng-click="addOne()"]').click()
        time.sleep(1)



    def deleteAll(self,deleteName):
        if deleteName == 'course':
            self.driver.find_element_by_css_selector('[ui-sref="course"]').click()
            time.sleep(1)
        elif deleteName == 'teacher':
            self.driver.find_element_by_css_selector('[ui-sref="teacher"]').click()
            time.sleep(1)
        elif deleteName == 'train':
            self.driver.find_element_by_css_selector('[ui-sref="training"]').click()
            time.sleep(1)
        elif deleteName == 'trainGrade':
            self.driver.find_element_by_css_selector('[ui-sref="traininggrade"]').click()
            time.sleep(1)
        else:
            raise Exception('unknow delete name %s' % deleteName)

        self.driver.implicitly_wait(2)

        while True:
            deletes = self.driver.find_elements_by_css_selector('*[ng-click^=delOne]')

            if deletes == []:
                break

            deletes[0].click()
            # time.sleep(1)
            self.driver.find_element_by_css_selector('.modal-footer  .btn-primary').click()

            time.sleep(1)

        self.driver.implicitly_wait(10)



    def getCourseList(self):
        self.driver.find_element_by_css_selector('[ui-sref="course"]').click()
        eles = self.driver.find_elements_by_css_selector('tbody tr td:nth-child(2)')
        return  [ele.text for ele in eles]


    def getTeacherList(self):
        self.driver.find_element_by_css_selector('[ui-sref="teacher"]').click()
        eles = self.driver.find_elements_by_css_selector('tbody tr td:nth-child(2)')
        return  [ele.text for ele in eles]


    def getTrainList(self):
        self.driver.find_element_by_css_selector('[ui-sref="training"]').click()
        eles = self.driver.find_elements_by_css_selector('tbody tr td:nth-child(2)')
        return  [ele.text for ele in eles]


    def getTrainGradeList(self):
        self.driver.find_element_by_css_selector('[ui-sref="traininggrade"]').click()
        eles = self.driver.find_elements_by_css_selector('tbody tr td:nth-child(2)')
        return  [ele.text for ele in eles]

























































































































































































