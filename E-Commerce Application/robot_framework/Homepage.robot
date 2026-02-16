*** Settings ***
Library    SeleniumLibrary
Suite Setup    Open Kate Spade
Suite Teardown    Close Browser

*** Variables ***
${URL}        https://www.katespade.com
${BROWSER}    Chrome
${TIMEOUT}    15s

*** Keywords ***
Open Kate Spade
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Timeout    ${TIMEOUT}
    Wait Until Page Contains Element    css=a[href*='login']

Click Account Icon
    # This targets the account icon anchor element
    Click Element    css=a[href*='login']

Verify Login Page
    Wait Until Location Contains    login    timeout=10s

*** Test Cases ***
TC01 Click Account Icon
    Click Account Icon
    Verify Login Page
