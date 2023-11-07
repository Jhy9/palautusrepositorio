*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kaapo
    Set Password  salasana1123
    Set Password Confirmation  salasana1123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  salasana1123
    Set Password Confirmation  salasana1123
    Submit Credentials
    Register Should Fail With Message  Username is too short

Register With Valid Username And Invalid Password
    Set Username  kaapola
    Set Password  salasana
    Set Password Confirmation  salasana
    Submit Credentials
    Register Should Fail With Message  Invalid password

Register With Nonmatching Password And Password Confirmation
    Set Username  kaapoaf
    Set Password  salasana123
    Set Password Confirmation  salasana321
    Submit Credentials
    Register Should Fail With Message  Passwords do not match

Login After Successful Registration
    Set Username  kaapos
    Set Password  salasana1123
    Set Password Confirmation  salasana1123
    Submit Credentials
    Go To Login Page
    Set Username  kaapos
    Set Password  salasana1123
    Submit Login Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  kuuka
    Set Password  salasana1123
    Set Password Confirmation  salasana321
    Submit Credentials
    Go To Login Page
    Set Username  kuuka
    Set Password  salasana1123
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password


*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation} 

Submit Credentials
    Click Button  Register

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Submit Login Credentials
    Click Button  Login
