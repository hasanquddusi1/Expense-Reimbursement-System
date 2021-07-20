# Manger Portal Feature File
Feature: Manager Portal

    # 1
    Scenario: A Manager is on the home page of Expense Reimbursement System and would like to login
        Given A manager is on the home page of Expense Reimbursement System
        When the manager clicks on the manager login button
        Then the manager is redirected to the manager login portal

    # 2
    Scenario: A Manager is on the login portal of Manager and would like to login with correct credentials.
        Given A manager is on the manager login portal
        Then a manager enters the correct username and the correct password
        When the manager clicks the login button
        Then the manager is redirected to the manager view page

