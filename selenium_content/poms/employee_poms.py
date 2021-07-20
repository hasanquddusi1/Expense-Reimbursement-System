
class Homepage:
    employee_login_id = 'emp_login'

    def __init__(self, driver):
        self.driver = driver

    def click_employee_login(self):
        self.driver.find_element_by_id(self.employee_login_id).click()


class EmployeeLoginPage:
    username_box_id = 'usr'
    password_box_id = 'pwd'
    login_button_id = 'login_button'

    def __init__(self, driver):
        self.driver = driver

    def enter_credentials(self):
        self.driver.find_element_by_id(
            self.username_box_id).send_keys('hubert.m')
        self.driver.find_element_by_id(self.password_box_id).send_keys('123')

    def click_login_button(self):
        self.driver.find_element_by_id(self.login_button_id).click()
