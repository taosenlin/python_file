*** Settings ***
Library    pylib.WebOpAdmin


*** Keywords ***
websetup
    setupWebTest     chrome


webteardown
    tearDownWebTest
