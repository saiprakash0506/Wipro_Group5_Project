*** Settings ***
Resource    ../keywords/ecommerce_keywords.robot
Suite Setup    Open Website
Suite Teardown    Close Website

*** Test Cases ***
User Can Remove Product From Cart
    Login To Application
    Add Four Products To Cart
    Go To Cart
    Remove All Items From Cart
    Page Should Not Contain Element    css=.cart_item
