*** Settings ***
Library     pylib.SchoolTeacherLib
Library     pylib.SchoolClassLib
Variables    cfg.py

*** Test Cases ***

添加老师2 - tc001002

    ${ret_add_teacher}=    add_school_teacher     xiaowu   小吴
                     ...               ${g_mid_science_id}
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





添加老师3 - tc001003

    ${ret_list_teacher1}=      list_school_teacher

    ${ret_add_teacher}=    add_school_teacher     xiaotao   小陶
                     ...               ${g_mid_science_id}
                     ...               ${isSaveId}
                     ...               15888888899   wl@qq.com   21000000000000022

    should be true     $ret_add_teacher['retcode']==1
    should be true     $ret_add_teacher['reason']=='登录名 xiaotao 已经存在'

    ${ret_list_teacher2}=      list_school_teacher

    should be true     $ret_list_teacher1==$ret_list_teacher2

    [Teardown]        delete school teacher       &{ret_add_teacher}[id]




修改老师1 - tc001051

    ${ret_modify_teacher}=       modify school teacher      99999999

    should be true        $ret_modify_teacher['retcode']==1
    should be true        $ret_modify_teacher['reason']=='id 为`99999999`的老师不存在'




修改老师2 - tc001052

    ${ret_add_class}=      add_school_class   ${g_grade7_id}   2班   60   isSaveClass2Id
    should be true           $ret_add_class['retcode']==0

    ${ret_add_teacher}=    add_school_teacher     xiaolan   小兰
                     ...               ${g_mid_science_id}
                     ...               ${isSaveId}
                     ...               15888888899   wl@qq.com   21000000000000022
                     ...               isSaveTeach2Id


    ${ret_modify_teacher}=      modify school teacher       ${isSaveTeach2Id}
                       ...      realname=小皇
                       ...      subjectid=${g_mid_science_id}              #classlist依赖于subjectid,缺少会出现问题
                       ...      classlist=${isSaveId},${isSaveClass2Id}
    sleep  1d

    should be true     $ret_modify_teacher['retcode']==0

    ${ret_list_teacher}=      list_school_teacher
    ${fc}=           evaluate      $ret_list_teacher['retlist'][1]

    should be true       $fc['realname']=='小皇'
    should be true       $fc['teachclasslist']==[${isSaveId},${isSaveClass2Id}]


    [Teardown]          run keywords          delete school teacher       ${isSaveTeach2Id}       AND
                                  ...          delete school class         ${isSaveClass2Id}





删除老师1 - tc001081

    ${ret_delete_teacher}=     delete school teacher     99999999
    should be true      $ret_delete_teacher['retcode']==404
    should be true      $ret_delete_teacher['reason']=='id 为`99999999`的老师不存在'




删除老师2 - tc001082

    ${ret_list_teacher1}=      list_school_teacher

    ${ret_add_teacher}=    add_school_teacher     xiaowu   小吴
                     ...               ${g_mid_science_id}
                     ...               ${isSaveId}
                     ...               15888888899   wl@qq.com   21000000000000022
                     ...               isTeachScienceSaveId

    ${ret_delete_teacher}=     delete_school_teacher      ${isTeachScienceSaveId}
    should be true      $ret_delete_teacher['retcode']==0

    ${ret_list_teacher2}=      list_school_teacher

    should be true     $ret_list_teacher1==$ret_list_teacher2









