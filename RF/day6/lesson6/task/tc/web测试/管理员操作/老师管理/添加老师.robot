*** Settings ***
Resource  rflib/rc.robot

*** Test Cases ***
添加老师
    #方法1，将初始化的关键字组合成一个用户关键字
#    [Setup]   addteacherSetup
    #方法2，
    [Setup]   run keywords    deleteAllTeachers
    ...       AND             deleteAllLesson
    ...       AND    addCourse    初中数学   数学描述   2
    ...       AND    addCourse    初中语文   语文描述   1
    [Teardown]   run keywords   deleteAllTeachers  AND deleteAllLesson

    #添加老师
    add teacher   小陈老师   xiaochen   数学老师   1   初中数学

    checkTeacher  小陈老师


*** Keywords ***
addteacherSetup
    loginwebsite
    #先删除老师再删除课程，因为需要后删除被关联的数据
    deleteAllTeachers
    deleteAllLesson
    addCourse    初中数学   数学描述   2
    addCourse    初中语文   语文描述   1
