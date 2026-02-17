*** Settings ***
Resource    ../keywords/ecommerce_keywords.robot
Suite Setup    Open Website
Suite Teardown    Close Website

*** Test Cases ***
User Can Complete Checkout Successfully
    Login To Application

    # Sort items low to high
    Sort Products Low To High

    # Add first 3 products
    Add Four Products To Cart

    # Verify badge shows 3
    ${count}=    Get Text    css=.shopping_cart_badge
    Should Be Equal    ${count}    4
    Sleep    ${DELAY}

    # Go to cart
    Go To Cart

    # Checkout process
    Click Button    id=checkout
    Sleep    ${DELAY}

    Input Text    id=first-name    John
    Sleep    ${DELAY}
    Input Text    id=last-name     Snow
    Sleep    ${DELAY}
    Input Text    id=postal-code   12345
    Sleep    ${DELAY}

    Click Button    id=continue
    Sleep    ${DELAY}

    Click Button    id=finish
    Sleep    ${DELAY}

    Page Should Contain    Thank you for your order!
