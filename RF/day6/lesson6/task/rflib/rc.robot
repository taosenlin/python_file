*** Settings ***
Library  SeleniumLibrary
Variables  cfg.py

#资源文件和套件文件的唯一区别是
#资源文件没有测试用例表，不可以存在测试用例


*** Keywords ***
loginwebsite
    #输入用户名密码
    go to  http://localhost/mgr/login/login.html
    input text  id:username   &{user1}[name]
    input text  id=password   &{user1}[pwd]
    click element  tag=button

addCourse
#开始添加课程
    [Arguments]   ${name}   ${desc}   ${idx}
    #进入课程
    click element  css=[ui-sref="course"]

    click element   css:[ng-click="showAddOne=true"]
    input text      css=input[ng-model='addData.name']    ${name}
    input text      css=textarea[ng-model='addData.desc']    ${desc}
    input text      css=input[ng-model='addData.display_idx']   ${idx}

    click element   css=[ng-click="addOne()"]
    sleep  1

checkCourse
    [Arguments]     ${expect}
#    ${course_name}    get text   css=tbody td:nth-child(2)
#    should be equal   ${expect}   ${course_name}
    #进入课程
    click element  css=[ui-sref="course"]
    #判断添加的课程包含在课程列表中
    ${eles}  get webelements  css=tbody td:nth-child(2)

    ${courses}   evaluate   [ele.text for ele in $eles]

    should be true    $expect in $courses

deleteAllLesson
    #进入课程
    click element  css=[ui-sref="course"]

    #删除课程
    set selenium implicit wait  1

    FOR  ${var}   IN RANGE   9999
        ${del_btns}   get webelements  css=[ng-click="delOne(one)"]
        exit for loop if  $del_btns==[]
        evaluate   $del_btns[0].click()

        click element  css=.btn-primary
        sleep   1    #为了等待弹出框消失，好接下来点击下面的删除按钮
    END
    set selenium implicit wait  1


deleteAllTeachers
    #进入老师界面
    click element  css=[ui-sref="teacher"]

    #删除所有老师
    set selenium implicit wait  1

    FOR  ${var}   IN RANGE   9999
        ${del_btns}   get webelements  css=[ng-click="delOne(one)"]
        exit for loop if  $del_btns==[]
        evaluate   $del_btns[0].click()

        click element  css=.btn-primary
        sleep   1    #为了等待弹出框消失，好接下来点击下面的删除按钮
    END
    set selenium implicit wait  1


add teacher
    [Arguments]  ${realname}  ${username}  ${desc}  ${idx}  ${course}
    #进入老师界面
    click element  css=[ui-sref="teacher"]

    click element   css:[ng-click="showAddOne=true"]
    input text      css=input[ng-model="addEditData.realname"]    ${realname}
    input text      css=[ng-model="addEditData.username"]   ${username}
    input text      css=textarea[ng-model="addEditData.desc"]    ${desc}
    input text      css=input[ng-model='addEditData.display_idx']   ${idx}
    #选择关联课程
    select from list by label   css=[ng-model*="courseSelected"]     ${course}
    click element    css=[ng-click="addEditData.addTeachCourse()"]

    click element   css=[ng-click="addOne()"]
    sleep  1

checkTeacher
    [Arguments]     ${expect}
#    ${course_name}    get text   css=tbody td:nth-child(2)
#    should be equal   ${expect}   ${course_name}
    #进入老师
    click element  css=[ui-sref="teacher"]
    #判断添加的课程包含在课程列表中
    ${eles}  get webelements  css=tbody td:nth-child(2)

    ${teachers}   evaluate   [ele.text for ele in $eles]

    should be true    $expect in $teachers


setupWebTest
    open browser  http://localhost/mgr/login/login.html   chrome
    set selenium implicit wait  10

teardownWebTest
    close browser