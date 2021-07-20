from selenium import webdriver
from selenium_content.poms.employee_poms import *
from selenium_content.poms.manager_poms import *


def before_all(context):
    context.driver = webdriver.Chrome()
    context.homepage = Homepage(context.driver)
    context.emp_login_page = EmployeeLoginPage(context.driver)

    context.homepage_for_manager = ManagerHomepage(context.driver)
    context.manager_login_page = ManagerLoginPage(context.driver)


def after_all(context):
    context.driver.quit()
