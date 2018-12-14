from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
from fixture.actions import ActionsHelper


class Application:
    base_url=""
    def __init__(self, browser="firefox",base_url="http://localhost/addressbook/"):
        self.address=base_url
        if browser == "firefox":
            self.wd = webdriver.Firefox()
            #открывать браузер на втором мониторе !!!
            self.wd.set_window_position(2000,0)
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











