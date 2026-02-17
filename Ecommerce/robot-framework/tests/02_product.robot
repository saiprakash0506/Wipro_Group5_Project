*** Settings ***
Resource    ../keywords/ecommerce_keywords.robot
Suite Setup    Open Website
Suite Teardown    Close Website

*** Test Cases ***
User Can View Product Details
    Login To Application
    Click Element    xpath=//div[text()='Sauce Labs Backpack']
    Wait Until Element Is Visible    css=.inventory_details_name
    Sleep    ${DELAY}
    Element Should Be Visible    css=.inventory_details_price
