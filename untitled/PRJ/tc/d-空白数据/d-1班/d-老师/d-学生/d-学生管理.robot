*** Settings ***
Library      pylib.SchoolStudentLib
Variables    cfg.py


*** Test Cases ***

添加学生2 - tc002002

    sleep   1d
    ${ret_add_student}=      add_school_student    xiaoruan    小阮    ${g_grade7_id}
                                            ...    ${isSaveId}
                                            ...    15888888877
    should be true           $ret_add_student['retcode']==0

    ${ret_list_student}=      list_school_student

    studentlist_should_contain       &{ret_list_student}[retlist]
                           ...       ${isSaveId}
                           ...       &{ret_add_student}[id]
                           ...       15888888877
                           ...       小阮
                           ...       xiaoruan

    [Teardown]      delete school student     &{ret_add_student}[id]




删除学生 - tc002081

    ${ret_list_student1}=       list_school_student

    ${ret_add_student}=      add_school_student    xiaogao   小高    ${g_grade7_id}
                                            ...    ${isSaveId}
                                            ...    15888888899
                                            ...    isStudentSaveId

    ${ret_delete_student}=      delete_school_student       ${isStudentSaveId}

    should be true         $ret_delete_student['retcode']==0

    ${ret_list_student2}=       list_school_student

    should be true      $ret_list_student1==$ret_list_student2


















