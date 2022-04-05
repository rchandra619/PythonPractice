*** Settings ***
Library     SeleniumLibrary

Library               RequestsLibrary
Library     ../Pyhton Files/Utills.py



*** Variables ***
${Base_url}     http://thetestingworldapi.com/



*** Test Cases ***
TC001_Get_Request
    Create Session    getStudentDetails    ${Base_url}
    ${response}=    GET On Session  getStudentDetails    api/studentsDetails
    Log To Console    ${response.content}+' hfkjdsbflsdkjfdfnfnfknfllkfnsldsfkndfndnfksdkdflkfn'

