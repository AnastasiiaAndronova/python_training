
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_homepage(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()
        WebDriverWait(wd, 5).until(EC.presence_of_element_located((By.NAME, "searchstring")))

    def force_navigate_homepage(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        WebDriverWait(wd, 5).until(EC.presence_of_element_located((By.NAME, "searchstring")))

    def open_add_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def create(self, Contact):
        wd = self.app.wd
        self.open_add_contact_page()
        self.fill_the_form(Contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def fill_the_form(self, Contact):
        self.app.actions.change_field_value("firstname", Contact.firstname)
        self.app.actions.change_field_value("middlename", Contact.middlename)
        self.app.actions.change_field_value("lastname", Contact.lastname)
        self.app.actions.change_field_value("nickname", Contact.nickname)
        # if Contact.photo is not None:
        #     wd.find_element_by_name("photo").send_keys(Contact.photo)
        self.app.actions.change_field_value("title", Contact.title)
        self.app.actions.change_field_value("company", Contact.company)
        self.app.actions.change_field_value("address", Contact.address)
        self.app.actions.change_field_value("home", Contact.home)
        self.app.actions.change_field_value("address2", Contact.address2)
        self.app.actions.change_field_value("mobile", Contact.mobile)
        self.app.actions.change_field_value("work", Contact.work)
        self.app.actions.change_field_value("fax", Contact.fax)
        self.app.actions.change_field_value("email", Contact.email)
        self.app.actions.change_field_value("email2", Contact.email2)
        self.app.actions.change_field_value("email3", Contact.email3)
        self.app.actions.change_field_value("homepage", Contact.homepage)
        self.app.actions.select_in_dropdown("bday", Contact.birthday_day)
        self.app.actions.change_field_value("byear", Contact.birthday_year)
        self.app.actions.select_in_dropdown("bmonth", Contact.birthday_month)
        self.app.actions.select_in_dropdown("aday", Contact.anniversary_day)
        self.app.actions.select_in_dropdown("amonth", Contact.anniversary_month)
        self.app.actions.change_field_value("ayear", Contact.anniversary_year)
        self.app.actions.change_field_value("address2", Contact.address2)
        self.app.actions.change_field_value("phone2", Contact.phone2)
        self.app.actions.change_field_value("notes", Contact.notes)

    def modify_first(self, Contact):
        wd = self.app.wd
        self.app.contact.force_navigate_homepage()
        # open first contact for edit
        WebDriverWait(wd, 5).until(EC.presence_of_element_located((By.NAME, "selected[]")))
        wd.find_element_by_name("selected[]").click()
        WebDriverWait(wd, 5).until(EC.presence_of_element_located((By.XPATH, "//img[@alt='Edit']")))
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_the_form(Contact)
        # Submit contact editing
        wd.find_element_by_name("update").click()

    def delete_first(self):
        wd = self.app.wd
        self.app.contact.force_navigate_homepage()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        WebDriverWait(wd, 5).until(EC.alert_is_present())
        wd.switch_to.alert.accept()
        WebDriverWait(wd, 5).until(EC.presence_of_element_located((By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Record successful deleted'])[1]/preceding::h1[1]")))



