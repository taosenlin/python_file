*** Settings ***
Suite Setup       log to console    \n--- Suite __init__ Setup ---
#Suite Setup       fail
Suite Teardown    log to console    \n--- Suite __init__ Teardown ---
Test Setup       log to console    \n--- Test __init__ Default Setup ---
Test Teardown    log to console    \n--- Test __init__ Default Teardown ---
