*** Settings ***
Resource    ../keywords/ecommerce_keywords.robot
Suite Setup    Open Website
Suite Teardown    Close Website

*** Test Cases ***
User Logout And Session Validation
    Login To Application
    Logout From Application
    Wait Until Element Is Visible    id=login-button    timeout=10s
    Location Should Contain    saucedemo.com
