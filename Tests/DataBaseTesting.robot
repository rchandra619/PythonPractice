*** Settings ***
Library     DatabaseLibrary
Library     OperatingSystem
Suite Setup     Connect to DB sql3480709
Suite Teardown      Disconnect from DB sql3480709


*** Variables ***

${DataBaseName}     sql3480709
${DBUser}           sql3480709
${DBPassword}       8IWCklEhG6
${Port}             3306
${DBHost}           sql3.freesqldatabase.com


*** Test Cases ***
#Creating Person table in sql3480709 DataBase
#    Create Table in DB sql3480709

Insert Data into Database Person table
    #Insert multipule data in DB
    Checking data if exist in DB
    Check rows in table

*** Keywords ***
Connect to DB sql3480709
    ${isconnected}=     Connect To Database     pymysql   ${DataBaseName}     ${DBUser}     ${DBPassword}     ${DBHost}     ${Port}
    Log To Console    ${isconnected}


Disconnect from DB sql3480709
    Disconnect From Database

Create Table in DB sql3480709

    ${Output}=      Execute Sql String    Create table person(id integer,first_name varchar(20),last_name varchar(20));
    Log To Console    ${Output}
Insert multipule data in DB
    ${isInserted}=      Execute Sql String    insert into person values(101,"Ravi","Chandra");
    Execute Sql String    insert into person values(102,"ram","Charan");
    Execute Sql String    insert into person values(103,"NTR","JR");
    Execute Sql String    insert into person values(104,"Rajamouli","SS");

    Log To Console    ${isInserted}
Checking data if exist in DB
    Check If Exists In Database    select id from sql3480709.person where last_name="SS";
    #Log To Console    ${Result}

Check rows in table
    ${Rows}=    Row Count Is Equal To X    select id from sql3480709.person    9
    Log To Console    ${Rows}