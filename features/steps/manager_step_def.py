from behave import *
# Manager portal step file

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                                                 STEP 1


@given('A manager is on the home page of Expense Reimbursement System')
def home_page(context):
    context.driver.get('http://127.0.0.1:5000/home')


@when('the manager clicks on the manager login button')
def click_on_manager_login(context):
    context.homepage_for_manager.click_manager_login()


@then('the manager is redirected to the manager login portal')
def redirect_to_manager_portal(context):
    context.driver.get('http://127.0.0.1:5000/admin')

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                                                 STEP 2


@given('A manager is on the manager login portal')
def test_manager_portal(context):
    context.driver.get('http://127.0.0.1:5000/admin')


@then('a manager enters the correct username and the correct password')
def test_manager_credentials(context):
    context.manager_login_page.enter_manager_credentials()


@when('the manager clicks the login button')
def test_manager_clicks_submit(context):
    context.manager_login_page.click_login_button_mgr()


@then('the manager is redirected to the manager view page')
def test_manager_redirected_after_using_submit(context):
    # For this flask route in app is configured to localhost/employee/login so:
    assert 'manager-view' in context.driver.current_url

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
