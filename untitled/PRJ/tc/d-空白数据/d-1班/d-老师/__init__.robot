*** Settings ***
Library     pylib.SchoolTeacherLib
Variables   cfg.py

Suite Setup        add_school_teacher     xiaotao   小陶   ${g_mid_math_id}    ${isSaveId}
                     ...      15888888866   tsl@qq.com   21000000000000011      isTeachSaveId
Suite Teardown     delete_school_teacher      ${isTeachSaveId}