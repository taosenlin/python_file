*** Settings ***
Library    pylib.SchoolClassLib
Library    pylib.SchoolTeacherLib
Library    pylib.SchoolStudentLib

Suite Setup        Run keywords           delete_all_school_student    AND
         ...                               delete_all_school_teacher    AND
         ...                               delete_all_school_class