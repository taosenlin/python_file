*** Settings ***
Resource  rflib/rc.robot
#若需要导入PythoN库文件
#Library  pylib.st



*** Test Cases ***
添加课程1
    [Setup]   run keywords    deleteAllLesson
    [Teardown]  deleteAllLesson
    [Template]  addCourseandcheck
    #接下来，直接填写用例所需的参数
    初中数学   数学描述   2
    初中语文   语文描述   1
    英语       英语描述   3
    高数      高数描述    4


#添加课程2
#    [Setup]   deleteAllLesson
#    [Teardown]  deleteAllLesson
#    #自定义数据驱动-适用于大规模的数据
#    ${datas}   getdataExcel   path
#    FOR  ${data}  IN  @{datas}
#        addCourseandcheck   ${data.name}   ${data.desc}   ${data.idx}
#    END

*** Keywords ***
addCourseandcheck
    [Arguments]   ${name}   ${desc}   ${idx}

    addCourse   ${name}   ${desc}  ${idx}

    checkCourse  ${name}

