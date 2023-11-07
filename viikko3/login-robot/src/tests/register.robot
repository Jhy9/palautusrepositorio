*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kaapo  salasana123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalevi  alsawrf123
    Output Should Contain  User with username kalevi already exists

Register With Too Short Username And Valid Password
    Input Credentials  ka  alsawrf123
    Output Should Contain  Username is too short

Register With Enough Long But Invald Username And Valid Password
    Input Credentials  kalevi123  aslitjijwt124124
    Output Should Contain  Invalid username

Register With Valid Username And Too Short Password
    Input Credentials  kaapo  salas
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kaapo  asdasdadiwjrq
    Output Should Contain  Invalid password
    
*** Keywords ***
Create User And Input New
    Create User  kalevi  salasana123
    Input New Command