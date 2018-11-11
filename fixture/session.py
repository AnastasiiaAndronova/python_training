from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
class SessionHelper:

    def __init__(self, app):
        self.app = app

    def logout(self):
        wb = self.app.wb
        wb.find_element_by_link_text("Logout").click()
     #   self.app.open_login_page() - c этим не работает
        WebDriverWait(wb, 5).until(EC.presence_of_element_located((By.ID, "LoginForm")))



    def login(self, user, password):
        wb = self.app.wb
        self.app.open_login_page()
        WebDriverWait(wb, 5).until(EC.presence_of_element_located((By.ID, "LoginForm")))
        wb.find_element_by_name("user").clear()
        wb.find_element_by_name("user").clear()
        wb.find_element_by_name("user").send_keys(user)
        wb.find_element_by_id("LoginForm").click()
        wb.find_element_by_name("pass").click()
        wb.find_element_by_name("pass").clear()
        wb.find_element_by_name("pass").send_keys(password)
        wb.find_element_by_xpath("//input[@value='Login']").click()
