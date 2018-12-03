from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
from fixture.actions import ActionsHelper
import os

class Application:
    address=""
    def __init__(self, browser="firefox",address="http://localhost/addressbook/"):
        self.address=address
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "edge":
            self.wd = webdriver.Edge()
        else:
            raise ValueError("Unrecognized browser %s" % browser)



        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.actions = ActionsHelper(self)

    def destroy(self):
        self.wd.quit()

    def open_login_page(self):
        wd = self.wd
        wd.get(self.address)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False











