#思路1：SeleniumLibrary
#思路2：python+selenium

*** Settings ***
Resource  rflib/rc.robot


*** Test Cases ***
老师1
    [Setup]  run keywords   deleteAllTeachers   AND   deleteAllLesson
    ...   AND    addCourse   初中语文    语文课    1
    ...   AND    addCourse   初中化学    化学课    2

    add teacher   小陶老师    xiaotao    语文老师   2   初中语文
    #检查老师是否被添加
    checkteacher   小陶老师
    add teacher   小王老师    xiaowang    化学老师   1   初中化学
    #检查老师是否被添加
    checkteacher   小王老师
    ${teachers}   getteachers
    should be true  $teachers==['小王老师', '小陶老师']




