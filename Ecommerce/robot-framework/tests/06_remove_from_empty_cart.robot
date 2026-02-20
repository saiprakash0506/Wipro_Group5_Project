*** Settings ***
Library           SeleniumLibrary
Library           Collections
Resource          ../keywords/ecommerce_keywords.robot
Suite Setup       Open Website
Suite Teardown    Close Website

*** Test Cases ***
Remove From Empty Cart Should Fail

    Log    ===== Executing Negative Test: Remove From Empty Cart =====

    # Disable auto screenshot for clean manual control
    Register Keyword To Run On Failure    Nothing

    Login To Application
    Go To Cart

    ${remove_buttons}=    Get WebElements    xpath=//button[text()='Remove']

    # If no remove buttons found → take screenshot and fail
    IF    not ${remove_buttons}

        ${path}=    Capture Page Screenshot    empty_cart_failure.png
        Log    <img src="${path}" width="600px">    html=True

        Fail    No items in cart but attempted to remove item.

    ELSE
        Log    Unexpected: Remove button exists.
    END

    # Re-enable auto screenshot for other tests
    Register Keyword To Run On Failure    Capture Page Screenshot
