from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
from fixture.actions import ActionsHelper


class Application:

    def __init__(self):
        self.wb = webdriver.Firefox()
        self.wb.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.actions = ActionsHelper(self)

    def destroy(self):
        self.wb.quit()

    def open_login_page(self):
        wb = self.wb
        wb.get("http://localhost/addressbook/")









