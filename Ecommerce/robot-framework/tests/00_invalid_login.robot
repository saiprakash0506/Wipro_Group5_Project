*** Settings ***
Library           OperatingSystem
Library           Collections
Library           String
Resource          ../keywords/ecommerce_keywords.robot
Suite Setup       Open Website
Suite Teardown    Close Website

*** Test Cases ***
Invalid Login From CSV
    ${file}=    Get File    ${CURDIR}/../data/invalid_login_data.csv
    ${lines}=   Split To Lines    ${file}
    ${data}=    Get Slice From List    ${lines}    1

    FOR    ${index}    ${row}    IN ENUMERATE    @{data}

        Log    \n===== Executing Invalid Login Dataset ${index + 1} =====

        ${columns}=    Split String    ${row}    ,
        ${username}=   Get From List    ${columns}    0
        ${password}=   Get From List    ${columns}    1

        Input Text    id=user-name    ${username}
        Input Text    id=password     ${password}
        Click Button  id=login-button

        Wait Until Page Contains Element
        ...    css=h3[data-test="error"]
        ...    timeout=5s

        ${pass_missing}=    Run Keyword And Return Status
        ...    Page Should Contain    Password is required

        ${user_missing}=    Run Keyword And Return Status
        ...    Page Should Contain    Username is required

        ${invalid_match}=    Run Keyword And Return Status
        ...    Page Should Contain    Username and password do not match

        IF    ${pass_missing} or ${user_missing} or ${invalid_match}

            ${path}=    Capture Page Screenshot
            ...    invalid_login_${index + 1}.png

            Log    <img src="${path}" width="600px">    html=True

            Log    ✅ Expected validation message displayed

        ELSE
            Fail    Unexpected error message for dataset ${index + 1}
        END

        Go To    ${URL}

    END


