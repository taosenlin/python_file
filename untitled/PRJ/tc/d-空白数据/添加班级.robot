*** Settings ***
Library    pylib.SchoolClassLib
Variables  cfg.py

*** Test Cases ***

添加班级1 - tc000001

    ${ret_add}=   add_school_class   ${g_grade7_id}   1班   60
    should be true      $ret_add['retcode']==0

    ${ret_list}=    list_school_class    ${g_grade7_id}
    ${fc}           evaluate     $ret_list['retlist'][0]
    should be true     $fc['grade__name']=='七年级'
    should be true     $fc['name']=='1班'
    should be true     $fc['studentlimit']==60
    should be true     $fc['id']==$ret_add['id']
    should be true     $fc['invitecode']==$ret_add['invitecode']


    [Teardown]      delete_school_class    &{ret_add}[id]
