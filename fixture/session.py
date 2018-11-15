from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
class SessionHelper:

    def __init__(self, app):
        self.app = app

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()
        WebDriverWait(wd, 5).until(EC.presence_of_element_located((By.ID, "LoginForm")))



    def login(self, user=None, password=None):
        wd = self.app.wd
        self.app.open_login_page()
        WebDriverWait(wd, 5).until(EC.presence_of_element_located((By.ID, "LoginForm")))
        if user is None and password is None:
            # тестовый админ (пока у нас только одна роль и аккаунт)
            user = "admin"
            password = "secret"
        self.app.actions.change_field_value("user", user)
        self.app.actions.change_field_value("pass", password)
        wd.find_element_by_xpath("//input[@value='Login']").click()
