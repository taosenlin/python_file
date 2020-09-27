*** Settings ***
Library   pylib.SchoolTeacherLib
Library   pylib.SchoolClassLib
Variables  cfg.py

*** Test Cases ***

添加老师1 - tc001001

    ${ret_add_teacher}=    add_school_teacher     xiaowu   小吴
                     ...               ${g_mid_math_id}
                     ...               ${isSaveId}
                     ...               15888888899   wl@qq.com   21000000000000022

    should be true     $ret_add_teacher['retcode']==0

    ${ret_list_teacher}=      list_school_teacher


    teacherlist_should_contain          &{ret_list_teacher}[retlist]
                           ...          xiaowu    小吴
                           ...          &{ret_add_teacher}[id]
                           ...          ${isSaveId}
                           ...          15888888899
                           ...          wl@qq.com
                           ...          21000000000000022

    [Teardown]        delete school teacher       &{ret_add_teacher}[id]
