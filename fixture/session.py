from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
class SessionHelper:

    def __init__(self, app):
        self.app = app


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

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()
        WebDriverWait(wd, 3).until(EC.presence_of_element_located((By.ID, "LoginForm")))

    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def ensure_login(self,username,password):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as_username(username):
                return
            else:
                self.logout()
        self.login(username, password)

    def is_logged_in_as_username(self, username):
        wd = self.app.wd
        return self.get_logged_user() == username


    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element_by_xpath("//div/div[1]/form/b").text[1:-1]


