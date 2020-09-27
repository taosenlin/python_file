*** Settings ***
Library      pylib.SchoolStudentLib
Variables    cfg.py

Suite Setup        add_school_student    xiaoyu   小余    ${g_grade7_id}
                                            ...    ${isSaveId}
                                            ...    15888888866
                                            ...    isStuSaveId
Suite Teardown     delete_school_student    ${isStuSaveId}