
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_to_home_page(self):
        wb = self.app.wb
        wb.find_element_by_link_text("home page").click()

    def navigate_to_home_page(self):
        wb = self.app.wb
        wb.find_element_by_link_text("home").click()
        WebDriverWait(wb, 5).until(EC.presence_of_element_located((By.ID, "content")))

    def open_add_contact_page(self):
        wb = self.app.wb
        wb.find_element_by_link_text("add new").click()

    def create(self, Contact):
        wb = self.app.wb
        self.open_add_contact_page()
        self.app.actions.change_field_value("firstname", Contact.firstname)
        self.app.actions.change_field_value("middlename", Contact.middlename)
        self.app.actions.change_field_value("lastname", Contact.lastname)
        self.app.actions.change_field_value("nickname", Contact.nickname)
        # if Contact.photo is not None:
        #     wb.find_element_by_name("photo").send_keys(Contact.photo)
        self.app.actions.change_field_value("title", Contact.title)
        self.app.actions.change_field_value("company", Contact.company)
        self.app.actions.change_field_value("address", Contact.address)
        self.app.actions.change_field_value("home", Contact.home)
        self.app.actions.change_field_value("address2", Contact.address2)
        self.app.actions.change_field_value("mobile", Contact.mobile)
        self.app.actions.change_field_value("work", Contact.work)
        self.app.actions.change_field_value("fax", Contact.fax)
        self.app.actions.change_field_value("email", Contact. email)
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
        wb.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def modify_first(self, Contact):
        wb = self.app.wb
        # open first contact for edit
        wb.find_element_by_name("selected[]").click()
        wb.find_element_by_xpath("//img[@alt='Edit']").click()

        self.app.actions.change_field_value("firstname", Contact.firstname)
        self.app.actions.change_field_value("middlename", Contact.middlename)
        self.app.actions.change_field_value("lastname", Contact.lastname)
        self.app.actions.change_field_value("nickname", Contact.nickname)
        # if Contact.photo is not None:
        #     wb.find_element_by_name("photo").send_keys(Contact.photo)
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
        # Submit contact editing
        
        wb.find_element_by_name("update").click()

    def delete_first(self):
        wb = self.app.wb
        wb.find_element_by_name("selected[]").click()
        wb.find_element_by_xpath("//input[@value='Delete']").click()
        WebDriverWait(wb, 5).until(EC.alert_is_present())
        Alert(wb).accept()


