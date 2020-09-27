#*** Settings ***
#Library    SeleniumLibrary
#Library    Collections
#Library    delete_course1
#Resource    rc.robot

#套件文件
*** Settings ***
Resource     rflib/rc.robot
#Suite Setup   websetup
#Suite Teardown   webteardown


*** Test Cases ***
测试1
    [Setup]     teachersetup
#    [Setup]  run keywords   deleteAllTeacher   AND   deleteAllCourse
#    ...   AND    addCourse   初中语文    语文课    1
#    ...   AND    addCourse   初中化学    化学课    2

    addTeacher     小陶    xiaotao     语文老师    2    初中语文
    checkTeacher     小陶

    addTeacher     小吴    xiaowu     化学老师    1    初中化学
    checkTeacher     小吴

    ${teachers}    getTeacher
    should be true    $teachers==['小吴','小陶']




*** Keywords ***
teachersetup
    deleteAllTeacher
    deleteAllCourse
    addCourse    初中语文     语文课     1
    addCourse    初中化学     化学课     2
    sleep   1























































































































