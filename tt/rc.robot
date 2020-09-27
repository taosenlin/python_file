# coding:utf8
# Time:2020-07-04 21:17
# Author:TSL

*** Settings ***
Library    SeleniumLibrary

#用户关键字
*** Keywords ***
loginwebsite
    open browser    http://localhost/mgr/login/login.html    chrome
    set selenium implicit wait    10
#    input text        id=username    auto
#    input text        id=password    sdfsdfsdf
    click element     css=.btn.btn-success
    click element     css=.nav.navbar-nav li:nth-child(2)


deleteAllTeacher
    loginwebsite
    set selenium implicit wait   1
    FOR    ${i}    IN RANGE    5
        ${del_list}    get webelements     css=tbody>.ng-scope td:nth-child(6) button:nth-child(2)
        evaluate       $del_list[0].click()
        click element       css=.btn.btn-primary
        sleep   1
    END
    close browser
