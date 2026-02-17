*** Settings ***
Resource    ../keywords/ecommerce_keywords.robot
Suite Setup    Open Website
Suite Teardown    Close Website

*** Test Cases ***
User Login Successful
    Login To Application
    Location Should Contain    inventory
