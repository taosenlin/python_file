*** Settings ***
Library  Collections
Library  SeleniumLibrary
Variables  cfg.py


*** Keywords ***
loginwebsite
    go to        ${url}
    input text    id=username   &{user1}[username]
    input text    id=password   &{user1}[pw]
    click element   css=.btn-success

addCourse
    [Arguments]  ${name}    ${desc}   ${idx}
    #进入课程菜单
    click element  css=[ui-sref="course"]
    #开始添加课程
    click element  css=[ng-click="showAddOne=true"]
    #课程名称
    input text     css=[ng-model="addData.name"]    ${name}
    #详情描述
    input text     css=[ng-model="addData.desc"]    ${desc}
    #展示次序
    input text     css=[ng-model="addData.display_idx"]   ${idx}
    #创建
    click element  css=[ng-click="addOne()"]


checkCourse
    [Arguments]  ${expect}
    #进入课程菜单
    click element  css=[ui-sref="course"]
    ${eles}   get webelements    css=tbody td:nth-child(2)
    ${courses}   evaluate   [ele.text for ele in $eles]
    #判断课程列表中是否包含已添加课程
    should be true  $expect in $courses

deleteAllLesson

    #进入课程菜单
    click element  css=[ui-sref="course"]
    #删除所有课程
    set selenium implicit wait  1

    FOR   ${i}  IN RANGE   9999

        ${del_btns}   get webelements   css=[ng-click="delOne(one)"]

        exit for loop if   $del_btns == []

        evaluate   $del_btns[0].click()

        #点击确认
        click element   css=.btn-primary
        #等待弹出框消失
        sleep    1
     END


websetup
   open browser  http://localhost   chrome
   set selenium implicit wait  10


webteardown
   close browser


deleteAllTeachers

    #进入老师菜单
    click element  css=[ui-sref="teacher"]

    #删除所有老师
    set selenium implicit wait  1

    FOR   ${i}  IN RANGE   9999

        ${del_btns}   get webelements   css=[ng-click="delOne(one)"]

        exit for loop if   $del_btns == []

        evaluate   $del_btns[0].click()

        #点击确认
        click element   css=.btn-primary
        #等待弹出框消失
        sleep    1
     END

addTeacher
    [Arguments]  ${realname}  ${username}   ${desc}   ${idx}  ${course}
    #进入老师菜单
    click element  css=[ui-sref="teacher"]
    #开始添加老师
    click element  css=[ng-click="showAddOne=true"]
    #老师姓名
    input text     css=[ng-model="addEditData.realname"]    ${realname}
    #登录名
    input text     css=[ng-model="addEditData.username"]    ${username}
    #详情描述
    input text     css=[ng-model="addEditData.desc"]    ${desc}
    #展示次序
    input text     css=[ng-model*="display_idx"]   ${idx}
    #授课信息
    select from list by label  css=[ng-model*="courseSelected"]   ${course}
    click element  css=[ng-click*="addTeachCourse()"]
    #创建
    click element  css=[ng-click="addOne()"]
    sleep  1


checkTeacher
    [Arguments]  ${expect}
    #进入老师菜单
    click element  css=[ui-sref="teacher"]
    ${eles}   get webelements    css=tbody td:nth-child(2)
    ${teahers}   evaluate   [ele.text for ele in $eles]
    #判断老师列表中是否包含已添加老师
    should be true  $expect in $teahers

getteachers
    ${eles}   get webelements    css=tbody td:nth-child(2)
    ${teachers}   evaluate   [ele.text for ele in $eles]
    [Return]  ${teachers}