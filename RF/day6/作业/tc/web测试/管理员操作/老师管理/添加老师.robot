*** Settings ***
Library   pylib.WebOpAdmin


*** Test Cases ***
添加老师1
    [Setup]    run keywords    deleteAll    teacher
    ...    AND    deleteAll    course
    ...    AND    addCourse    初中语文    初中语文    2
    ...    AND    addCourse    初中数学    初中数学    1

    [Teardown]     Run Keywords     deleteAll    teacher
    ...    AND    deleteAll    course


    addTeacher     小陶    xiaotao   小陶老师    2   初中语文
    ${teachers}    getTeacherList
    should be true     '小陶' in $teachers


   addTeacher     小吴    xiaowu   小吴老师    1   初中数学
    ${teachers}    getTeacherList
    should be true     '小吴' in $teachers



