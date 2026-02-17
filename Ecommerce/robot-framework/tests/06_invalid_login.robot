*** Settings ***
Resource    ../keywords/ecommerce_keywords.robot
Suite Setup    Open Website
Suite Teardown    Close Website

*** Test Cases ***
User Cannot Login With Invalid Credentials
    Input Text    id=user-name    invalid_user
    Input Text    id=password     wrong_password
    Click Button  id=login-button

    Wait Until Page Contains Element    css=h3[data-test="error"]    timeout=10s
    Page Should Contain    Username and password do not match
