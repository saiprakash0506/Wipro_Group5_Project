*** Settings ***
Library    SeleniumLibrary    run_on_failure=Nothing
Resource   ../variables/config.robot

*** Keywords ***
Open Website
    IF    '${BROWSER}' == 'Chrome'

        ${options}=    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys, selenium.webdriver
        ${temp_dir}=    Evaluate    __import__('tempfile').mkdtemp()

        ${prefs}=    Create Dictionary
        ...    credentials_enable_service=False
        ...    profile.password_manager_enabled=False
        ...    profile.default_content_setting_values.notifications=2

        Call Method    ${options}    add_experimental_option    prefs    ${prefs}

        ${incognito}=        Set Variable    --incognito
        ${disable_pw}=       Set Variable    --disable-features=PasswordLeakDetection
        ${disable_notify}=   Set Variable    --disable-notifications
        ${no_first}=         Set Variable    --no-first-run
        ${no_default}=       Set Variable    --no-default-browser-check
        ${maximize}=         Set Variable    --start-maximized
        ${profile}=          Set Variable    --user-data-dir=${temp_dir}

        Call Method    ${options}    add_argument    ${incognito}
        Call Method    ${options}    add_argument    ${disable_pw}
        Call Method    ${options}    add_argument    ${disable_notify}
        Call Method    ${options}    add_argument    ${no_first}
        Call Method    ${options}    add_argument    ${no_default}
        Call Method    ${options}    add_argument    ${maximize}
        Call Method    ${options}    add_argument    ${profile}

        Create WebDriver    Chrome    options=${options}
        Go To    ${URL}

    ELSE IF    '${BROWSER}' == 'Edge'
        Open Browser    ${URL}    Edge
        Maximize Browser Window

    ELSE IF    '${BROWSER}' == 'Firefox'
        ${ff_options}=    Evaluate    sys.modules['selenium.webdriver'].FirefoxOptions()    sys, selenium.webdriver
        Call Method    ${ff_options}    add_argument    -private
        Create WebDriver    Firefox    options=${ff_options}
        Go To    ${URL}
    END

    Wait Until Element Is Visible    id=user-name    timeout=10s
    Sleep    ${DELAY}


Close Website
    Sleep    ${DELAY}
    Close Browser

Login To Application
    Input Text    id=user-name    ${USERNAME}
    Sleep    ${DELAY}
    Input Text    id=password     ${PASSWORD}
    Sleep    ${DELAY}
    Click Button  id=login-button
    Wait Until Page Contains Element    css=.inventory_list
    Sleep    ${DELAY}

Add Four Products To Cart
    # Add first 4 products visible on page
    ${buttons}=    Get WebElements    xpath=//button[contains(text(),'Add to cart')]
    FOR    ${index}    IN RANGE    0    4
        Click Element    ${buttons}[${index}]
        Sleep    ${DELAY}
    END

Verify Cart Has Four Items
    ${count}=    Get Text    css=.shopping_cart_badge
    Should Be Equal    ${count}    4
    Sleep    ${DELAY}

Go To Cart
    Click Element    css=.shopping_cart_link
    Wait Until Page Contains    Your Cart
    Sleep    ${DELAY}

Remove All Items From Cart
    ${remove_buttons}=    Get WebElements    xpath=//button[text()='Remove']
    FOR    ${btn}    IN    @{remove_buttons}
        Click Element    ${btn}
        Sleep    ${DELAY}
    END

Logout From Application
    Click Element    id=react-burger-menu-btn
    Sleep    ${DELAY}
    Click Element    id=logout_sidebar_link
    Wait Until Element Is Visible    id=login-button
    Sleep    ${DELAY}

Sort Products Low To High
    Select From List By Value    css=.product_sort_container    lohi
    Sleep    ${DELAY}

Checkout With User Data
    [Arguments]    ${first_name}    ${last_name}    ${postal_code}

    Login To Application
    Sort Products Low To High
    Add Four Products To Cart
    Verify Cart Has Four Items
    Go To Cart

    Click Button    id=checkout

    Input Text    id=first-name    ${first_name}
    Input Text    id=last-name     ${last_name}
    Input Text    id=postal-code   ${postal_code}

    Click Button    id=continue

    ${success_page}=    Run Keyword And Return Status
    ...    Wait Until Element Is Visible    id=finish    timeout=3s

    IF    ${success_page}
        Click Button    id=finish
        Page Should Contain    Thank you for your order!
    ELSE
        Wait Until Page Contains Element    css=h3[data-test="error"]    timeout=3s
        Log    Validation error appeared for invalid data
        Fail    Invalid checkout data
    END

    Click Button    id=back-to-products
    Logout From Application

Attempt Invalid Login
    [Arguments]    ${username}    ${password}

    Input Text    id=user-name    ${username}
    Input Text    id=password     ${password}
    Click Button  id=login-button

    Wait Until Page Contains Element    css=h3[data-test="error"]    timeout=5s
    Page Should Contain    Username and password do not match


