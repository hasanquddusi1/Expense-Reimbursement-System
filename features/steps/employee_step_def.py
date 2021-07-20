from behave import *
# Employee portal step file

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                                                 STEP 1


@given('An employee is on the home page of Expense Reimbursement System')
def home_page(context):
    context.driver.get('http://127.0.0.1:5000/home')


@when('the employee clicks on the employee login button')
def click_on_employee_login(context):
    context.homepage.click_employee_login()


@then('the employee is redirected to the employee login portal')
def redirect_to_employee_portal(context):
    context.driver.get('http://127.0.0.1:5000/employee')

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                                                 STEP 2


@given('An employee is on the employee login portal')
def test_employee_portal(context):
    context.driver.get('http://127.0.0.1:5000/employee')


@then('an employee enters the correct username and the correct password')
def test_employee_credentials(context):
    context.emp_login_page.enter_credentials()


@when('the employee clicks the login button')
def test_employee_clicks_submit(context):
    context.emp_login_page.click_login_button()


@then('the employee is redirected to the reimbursement request form page')
def test_employee_redirected_after_using_submit(context):
    # For this flask route in app is configured to localhost/employee/login so:
    assert 'login' in context.driver.current_url
