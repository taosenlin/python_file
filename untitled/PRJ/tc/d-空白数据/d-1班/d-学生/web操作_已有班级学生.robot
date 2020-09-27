*** Settings ***
Library      pylib.WebOpLib
Library      pylib.SchoolTeacherLib
Variables    cfg.py

Suite Setup         setupBrowser
Suite Teardown     tearDownBrowser

*** Test Cases ***

老师登录2 - tc005002

    add_school_teacher     xiaotao   小陶   ${g_mid_math_id}    ${isSaveId}
                     ...      15888888866   tsl@qq.com   21000000000000011
                     ...      isTeachSaveId

    teacherLoginPage      xiaotao       888888

    ${teacher_home_info}=   teacher home page

    ${check_teacher_home_info}      create list     松勤学院01036   小陶    初中数学
                                            ...     0     0    0

    should be true     $teacher_home_info==$check_teacher_home_info

    ${teacher_class_student}=       teacher class student page

    should be true      $teacher_class_student=={'七年级1班':['小余']}

    [Teardown]     delete_school_teacher      ${isTeachSaveId}



