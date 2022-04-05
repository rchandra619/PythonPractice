*** Settings ***
Resource        ../DataBaseTesting.robot

Suite Setup     Connect to DB sql3480709
Suite Teardown      Disconnect from DB sql3480709

*** Test Cases ***
Creating Person table in sql3480709 DataBase
    Create Table in DB sql3480709