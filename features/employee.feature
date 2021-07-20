# Employee Portal Feature File
Feature: Employee Portal

    #1
    Scenario: An employee is on the home page of Expense Reimbursement System and would like to login
        Given An employee is on the home page of Expense Reimbursement System
        When the employee clicks on the employee login button
        Then the employee is redirected to the employee login portal

    #2
    Scenario: An employee is on the login portal of employee and would like to login with correct credentials.
        Given An employee is on the employee login portal
        Then an employee enters the correct username and the correct password
        When the employee clicks the login button
        Then the employee is redirected to the reimbursement request form page

