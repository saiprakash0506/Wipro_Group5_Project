*** Settings ***
Library           SeleniumLibrary
Library           OperatingSystem
Library           Collections
Library           String
Resource          ../keywords/ecommerce_keywords.robot
Suite Setup       Open Website
Suite Teardown    Close Website

*** Test Cases ***
Checkout With Multiple Users From CSV
    ${file}=    Get File    ${CURDIR}/../data/checkout_data.csv
    ${lines}=   Split To Lines    ${file}

    ${data}=    Get Slice From List    ${lines}    1

    FOR    ${row}    IN    @{data}
        ${columns}=      Split String    ${row}    ,
        ${first_name}=   Get From List    ${columns}    0
        ${last_name}=    Get From List    ${columns}    1
        ${postal_code}=  Get From List    ${columns}    2

        Checkout With User Data    ${first_name}    ${last_name}    ${postal_code}
    END
