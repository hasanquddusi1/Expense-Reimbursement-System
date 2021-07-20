from selenium_content.poms.employee_poms import EmployeeLoginPage, Homepage
from selenium import webdriver
driver = webdriver.Chrome()


driver.get("http://127.0.0.1:5000/home")
# Employee can access homepage
homepage = Homepage(driver)
homepage.click_employee_login()

driver.get("http://127.0.0.1:5000/employee")
# Employee can login using valid credentials
emp_login_page = EmployeeLoginPage(driver)
emp_login_page.enter_credentials()
emp_login_page.click_login_button()


driver.quit()
