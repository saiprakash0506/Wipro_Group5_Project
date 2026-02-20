*** Settings ***
Library           OperatingSystem
Library           Collections
Library           String
Resource          ../keywords/ecommerce_keywords.robot
Suite Setup       Open Website
Suite Teardown    Close Website

*** Test Cases ***
Checkout With Multiple Users From CSV
    Register Keyword To Run On Failure    Nothing

    ${file}=    Get File    ${CURDIR}/../data/checkout_data.csv
    ${lines}=   Split To Lines    ${file}
    ${data}=    Get Slice From List    ${lines}    1

    FOR    ${index}    ${row}    IN ENUMERATE    @{data}
        ${columns}=      Split String    ${row}    ,
        ${first_name}=   Get From List    ${columns}    0
        ${last_name}=    Get From List    ${columns}    1
        ${postal_code}=  Get From List    ${columns}    2

        TRY
            Checkout With User Data    ${first_name}    ${last_name}    ${postal_code}
        EXCEPT
            ${path}=    Capture Page Screenshot    checkout_fail_${index + 1}.png
            Log    <img src="${path}" width="600px">    html=True
        END

        Close Browser
        Open Website
    END

    Register Keyword To Run On Failure    Capture Page Screenshot


