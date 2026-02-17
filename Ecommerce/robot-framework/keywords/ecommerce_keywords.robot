*** Settings ***
Library    SeleniumLibrary
Resource   ../variables/config.robot

*** Keywords ***
Open Website
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed    0.3s
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

