
class ManagerHomepage:

    manager_login_id = 'mgr-login'

    def __init__(self, driver):
        self.driver = driver

    def click_manager_login(self):
        self.driver.find_element_by_id(self.manager_login_id).click()


class ManagerLoginPage:
    username_box_id = 'mgr-usr'
    password_box_id = 'mgr-pwd'
    login_button_id = 'login-button'

    def __init__(self, driver):
        self.driver = driver

    def enter_manager_credentials(self):
        self.driver.find_element_by_id(
            self.username_box_id).send_keys('tim12')
        self.driver.find_element_by_id(self.password_box_id).send_keys('123')

    def click_login_button_mgr(self):
        self.driver.find_element_by_id(self.login_button_id).click()
