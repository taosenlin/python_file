*** Settings ***
Library      pylib.SchoolStudentLib
Variables    cfg.py

*** Test Cases ***

添加学生1 - tc002001

    sleep    1d
    ${ret_add_student}=      add_school_student    xiaojun   小珺    ${g_grade7_id}
                                            ...    ${isSaveId}
                                            ...    15888888888

    should be true       $ret_add_student['retcode']==0

    ${ret_list_student}=     list_school_student

    studentlist_should_contain       &{ret_list_student}[retlist]
                           ...       ${isSaveId}
                           ...       &{ret_add_student}[id]
                           ...       15888888888
                           ...       小珺
                           ...       xiaojun

    [Teardown]      delete school student     &{ret_add_student}[id]














