*** Settings ***
Library   pylib.SchoolClassLib
Variables  cfg.py

Suite Setup       add_school_class   ${g_grade7_id}   1班   60   isSaveId
Suite Teardown    delete_school_class    ${isSaveId}