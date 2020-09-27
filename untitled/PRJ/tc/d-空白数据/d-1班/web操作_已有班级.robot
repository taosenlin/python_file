*** Settings ***
Library      pylib.WebOpLib
Library      pylib.SchoolTeacherLib
Library      pylib.SchoolStudentLib
Variables    cfg.py

Suite Setup         setupBrowser
Suite Teardown     tearDownBrowser

*** Test Cases ***

老师登录1 - tc005001

    add_school_teacher     xiaotao   小陶   ${g_mid_math_id}    ${isSaveId}
                     ...      15888888866   tsl@qq.com   21000000000000011
                     ...      isTeachSaveId

    teacherLoginPage      xiaotao       888888

    ${teacher_home_info}=   teacher home page

    ${check_teacher_home_info}      create list     松勤学院01036   小陶    初中数学
                                            ...     0     0    0

    should be true     $teacher_home_info==$check_teacher_home_info

    ${teacher_class_student}=       teacher class student page

    should be true      $teacher_class_student=={'七年级1班':[]}

    [Teardown]     delete_school_teacher      ${isTeachSaveId}




学生登录1 - tc005081

    add_school_student    xiaoyu   小余    ${g_grade7_id}
                            ...    ${isSaveId}
                            ...    15888888866
                            ...    isStuSaveId

    studentLoginPage      xiaoyu     888888

    ${student_home_info}=      student home page

    ${check_student_home_info}=     create list      小余      松勤学院01036
                                            ...      0     0

    ${ret_wrong_questions}=     student_wrong_questions
    should be true     $ret_wrong_questions=='您尚未有错题入库哦'

    [Teardown]     delete_school_student    ${isStuSaveId}
















































