from selenium_content.poms.manager_poms import *
from selenium import webdriver

driver = webdriver.Chrome()


driver.get("http://127.0.0.1:5000/home")
# Manager can access login Portal
homepage_for_manager = ManagerHomepage(driver)
homepage_for_manager.click_manager_login()


driver.get("http://127.0.0.1:5000/admin")
# Manager can login using his/her credentials
manager_login_page = ManagerLoginPage(driver)
manager_login_page.enter_manager_credentials()
manager_login_page.click_login_button_mgr()


driver.quit()
