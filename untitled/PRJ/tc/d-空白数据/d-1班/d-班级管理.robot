*** Settings ***
Library    pylib.SchoolClassLib
Variables  cfg.py

*** Test Cases ***

添加班级2 - tc000002

    ${ret_add}=   add_school_class   ${g_grade7_id}   2班   60

    should be true      $ret_add['retcode']==0

    ${ret_list}=    list_school_class    ${g_grade7_id}
    ${fc}           evaluate     $ret_list['retlist']

    classlist_should_contain      ${fc}
    ...  2班   七年级    &{ret_add}[invitecode]   60   0   &{ret_add}[id]



    [Teardown]      delete_school_class    &{ret_add}[id]





添加班级3 - tc000003


    ${list_before}=    list_school_class    ${g_grade7_id}

    ${ret_add}=   add_school_class   ${g_grade7_id}   1班   60
    should be true      $ret_add['retcode']==1
    should be true      $ret_add['reason']=='duplicated class name'

    ${list_after}=    list_school_class    ${g_grade7_id}




修改班级1 - tc000051

    ${ret_add}=      add_school_class   ${g_grade7_id}   2班   60

    ${ret_modify}=   modify school class   ${ret_add}[id]   5班   60
    should be true     $ret_modify['retcode']==0


    ${ret_list}=      list school class    ${g_grade7_id}
    ${fc}=            evaluate     $ret_list['retlist']

    classlist_should_contain      ${fc}
    ...  5班   七年级    &{ret_add}[invitecode]   60   0   &{ret_add}[id]

    [Teardown]      delete_school_class    &{ret_add}[id]




修改班级2 - tc000052

    ${ret_list1}=    list school class    ${g_grade7_id}

    ${ret_add}=      add_school_class   ${g_grade7_id}   1班   60

    ${ret_modify}=   modify school class   ${ret_add}[id]   2班   60
    should be true     $ret_modify['retcode']==1
    should be true     $ret_modify['reason']=='duplicated class name'

    ${ret_list2}=      list school class    ${g_grade7_id}

    should be true     $ret_list1==$ret_list2

    [Teardown]      delete_school_class    &{ret_add}[id]



修改班级3 - tc000053

    ${ret_modify}=   modify school class   9999999   2班   60

    should be true   $ret_modify['retcode']==404
    should be true   $ret_modify['reason']=='id 为`9999999`的班级不存在'



删除班级 - tc000081

    ${ret_delete}=     delete_school_class     9999999
    should be true   $ret_delete['retcode']==404
    should be true   $ret_delete['reason']=='id 为`9999999`的班级不存在'



删除班级 - tc000082

    ${ret_list1}=    list school class    ${g_grade7_id}

    ${ret_add}=      add_school_class   ${g_grade7_id}   2班   60

    ${ret_delete}=     delete_school_class     ${ret_add}[id]
    should be true     $ret_delete['retcode']==0


    ${ret_list2}=      list school class    ${g_grade7_id}

    should be true     $ret_list1==$ret_list2

