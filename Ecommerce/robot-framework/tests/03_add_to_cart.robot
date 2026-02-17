*** Settings ***
Resource    ../keywords/ecommerce_keywords.robot
Suite Setup    Open Website
Suite Teardown    Close Website

*** Test Cases ***
User Can Add Four Products To Cart
    Login To Application
    Add Four Products To Cart
    Verify Cart Has Four Items
    Go To Cart
    Page Should Contain    Your Cart
