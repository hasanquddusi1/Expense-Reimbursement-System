# Expense-Reimbursement-System
## Project Overview
Expense Reimbursement System (ERS) is a web application that allows users to sign-in and submit requests for reimbursing work related expenses. Managers can login and approve or deny requests. The project also provides automation tests using Selenium in Python.

## Technologies used

- Python
- Flask
- HTML5
- CSS3
- JavaScript
- Bootstrap
- Postgresql
- AWS RDS
- Selenium
- Cucumber


## Project Features

- Employees can login to the system and submit reimbursement requests.
- Employees can view a table of their past/pending requests.
- Managers can view all submitted requests and approve/deny requests.
- Managers can view statistics about submitted requests and optionally leave feedback to employees.

## Getting Started
Follow the steps provided below to run this project on your system.

- Install Python-version 3.9.
- Download all packages provided in pipfile.
- Create RDS instance on AWS and assign environment variables on your system for database connection.
- Run sql_script in Postgresql client (Dbeaver/PgAdmin) to initialize all database tables.
- Run main.py to start the application, the default port is set to localhost:5000.
- Browser automation tests will run with Selenium.
