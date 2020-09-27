#coding : utf8
#Author : taosenlin
#Time : 2020/7/27 14:08

from selenium import webdriver
import time
from cfg import *
from pprint import pprint


class WebOpLib:

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self):
        pass

    def setupBrowser(self):
        self.driver = webdriver.Chrome(chrome_driver1)
        self.driver.implicitly_wait(10)

    def tearDownBrowser(self):
        self.driver.quit()

    def teacherLoginPage(self,username,password):
        self.driver.get(g_teacher_url)
        self.driver.find_element_by_id("username").send_keys(username)
        self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element_by_id("submit").click()

        self.driver.find_element_by_id("topbar")


    def teacher_home_page(self):
        #进入老师主页
        self.driver.find_element_by_css_selector('a[href="#/home"] li').click()
        self.driver.find_element_by_id("home_div")
        time.sleep(2)

        eles = self.driver.find_elements_by_css_selector("#home_div .ng-binding")
        # print([ele.text for ele in eles])
        return [ele.text for ele in eles]



    def teacher_class_student_page(self):
        #点击班级情况
        self.driver.find_element_by_css_selector(".main-menu li:nth-of-type(4)").click()
        #进入班级学生页面
        self.driver.find_element_by_css_selector('a[href="#/student_group"] span').click()
        time.sleep(2)

        #找到班级列表
        classes = self.driver.find_elements_by_css_selector(".panel-green")
        if not classes:
            return {}

        classStuList = {}

        for cla in classes:
            #找到班级列表，取出班级姓名
            gradeName = cla.find_element_by_css_selector("#wrapper .panel-heading a").text.replace(' ','')
            #点击打开班级列表
            cla.click()
            time.sleep(2)

            self.driver.implicitly_wait(1)
            #取出班级所有学生
            stuList = cla.find_elements_by_css_selector("#wrapper tbody tr td:nth-child(2)")
            self.driver.implicitly_wait(10)

            #生成列表生成式
            stus = [ele.text for ele in stuList]
            classStuList[gradeName] = stus

        # print(classStuList)
        return classStuList




    def studentLoginPage(self,username,password):
        self.driver.get(g_student_url)
        self.driver.find_element_by_id("username").send_keys(username)
        self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element_by_id("submit").click()

        self.driver.find_element_by_id("wrapper")



    def student_home_page(self):
        #进入学生主页
        self.driver.find_element_by_css_selector('a[href="#/home"] li').click()
        self.driver.find_element_by_id("wrapper")
        time.sleep(2)

        eles = self.driver.find_elements_by_css_selector("#wrapper .ng-binding")
        #删除注册码(注册码无法获取)
        eles.pop(2)
        # print([ele.text for ele in eles])
        return [ele.text for ele in eles]



    def student_wrong_questions(self):
        self.driver.find_element_by_css_selector('a[href="#/yj_wrong_questions"] li').click()
        time.sleep(2)

        ret = self.driver.find_element_by_css_selector("#page-wrapper span").text

        # print(ret)
        return ret





    def teacher_assign_work(self,exam_name):
        self.driver.find_element_by_css_selector(".main-menu li:nth-of-type(2)").click()
        #点击创建作业
        self.driver.find_element_by_css_selector('a[ng-click="show_page_addexam()"] span').click()
        time.sleep(2)

        #输入作业名称
        self.driver.find_element_by_id("exam_name_text").send_keys(exam_name)
        #点击从题库选择题目
        self.driver.find_element_by_css_selector('div [ng-click="gotoPickQuestion()"]').click()

        time.sleep(2)

        #切换到iframe弹框内
        self.driver.switch_to.frame("pick_questions_frame")

        #选择加入试题篮
        pick_question = self.driver.find_elements_by_css_selector('div [class*="btn_pick_question"]')
        for ele in range(3,len(pick_question)):
            time.sleep(1)
            pick_question1 = self.driver.find_elements_by_css_selector('div [class*="btn_pick_question"]')
            pick_question1[ele].click()
            if ele == 5:
                break

        #点击确定
        self.driver.find_element_by_css_selector('div [onclick*="pickQuestionOK"]').click()

        #退出iframe弹框
        self.driver.switch_to.default_content()

        time.sleep(2)

        #点击确定添加
        self.driver.find_element_by_id('btn_submit').click()

        #点击发布给学生
        self.driver.find_element_by_css_selector('.bootstrap-dialog-footer button:nth-child(2)').click()

        #获取当前窗口的句柄
        mainWindow = self.driver.current_window_handle

        time.sleep(2)

        #获取当前打开的所有窗口的句柄
        handles = self.driver.window_handles
        for handle in handles:
            self.driver.switch_to.window(handle)
            if '下发学习任务' in self.driver.title:
                break

        #勾选下发任务的学生
        self.driver.find_element_by_css_selector('tbody .myCheckbox').click()

        #确定下发
        self.driver.find_element_by_css_selector('div [class*="btn-outlined"]').click()

        #点击确定
        self.driver.find_element_by_css_selector('[ng-click="dispatchIt()"]').click()
        self.driver.find_element_by_css_selector('[class="btn btn-default"]').click()

        #返回之前的窗口
        self.driver.switch_to.window(mainWindow)





    def student_finish_work(self):
        #点击我的任务
        self.driver.find_element_by_css_selector('a[href="#/task_manage"] li').click()
        #点击去做
        self.driver.find_element_by_css_selector('[ng-click="viewTask(taskTrack)"]').click()
        time.sleep(2)

        #选择答案
        do_work = self.driver.find_elements_by_css_selector('.btn-group button:nth-child(1)')
        for ele in do_work:
            ele.click()

        time.sleep(2)
        #点击提交
        self.driver.find_element_by_css_selector('[ng-click="saveMyResult(true)"]').click()
        #点击确定
        self.driver.find_element_by_css_selector('.bootstrap-dialog-footer button:nth-child(2)').click()





    def teacher_check_work(self):
        #点击作业
        # self.driver.find_element_by_css_selector('.main-menu li:nth-of-type(2)').click()
        # 点击已发布作业
        # self.driver.find_element_by_css_selector('.main-menu li:nth-of-type(2) [class="fa fa-bell-o"] span').click()
        # time.sleep(2)

        self.driver.get("http://ci.ytesting.com/teacher/index.html#/task_manage?tt=1")
        #点击完成情况
        self.driver.find_element_by_css_selector('.row tbody tr:nth-child(1) td:nth-child(5)').click()
        time.sleep(2)

        #点击查看
        self.driver.find_element_by_css_selector('[ng-click*="viewTaskTrack"]').click()

        #当前窗口的句柄
        mainWindow = self.driver.current_window_handle

        #获取所有打开窗口的句柄
        handles = self.driver.window_handles
        for handle in handles:
            self.driver.switch_to.window(handle)
            if '查看作业' in self.driver.title:
                break

        student_answer = self.driver.find_elements_by_css_selector('.myCheckbox input:checked + span')
        ret = [ele.find_element_by_xpath("./..").text.strip() for ele in student_answer]
        pprint(ret,indent=2)

        #切回主窗口
        self.driver.switch_to.window(mainWindow)

        return ret






















if __name__ == '__main__':
    webop = WebOpLib()
    webop.setupBrowser()
    webop.teacherLoginPage("xiaotao",888888)
    # webop.teacher_home_page()
    # webop.teacher_class_student_page()
    # webop.tearDownBrowser()

    # webop.studentLoginPage("xiaoyu",888888)
    # webop.student_home_page()
    # webop.student_wrong_questions()

    webop.teacher_assign_work('exam_math33')

    webop.studentLoginPage("xiaoyu", 888888)
    webop.student_finish_work()

    webop.teacherLoginPage("xiaotao", 888888)
    webop.teacher_check_work()
    webop.tearDownBrowser()























