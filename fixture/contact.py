
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_to_home_page(self):
        wb = self.app.wb
        wb.find_element_by_link_text("home page").click()

    def open_add_contact_page(self):
        wb = self.app.wb
        wb.find_element_by_link_text("add new").click()

    def create(self, Contact):
        wb = self.app.wb
        self.open_add_contact_page()
        # populate "add contact" fields
        # Хотелось сделать универсальный метод populate_form_fields но пока непонятно как лучше "правильно" хранить множество свойств для одних и тех же обьектов.
        print (Contact)
        self.app.actions.change_field_value("firstname", Contact.firstname)
        self.app.actions.change_field_value("middlename", Contact.middlename)
        self.app.actions.change_field_value("lastname", Contact.lastname)
        self.app.actions.change_field_value("nickname", Contact.nickname)
        if Contact.photo is not None:
            wb.find_element_by_name("photo").send_keys(Contact.photo)
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
        # populate "add contact" fields
        # Хотелось сделать универсальный метод populate_form_fields но пока непонятно как лучше "правильно" хранить множество свойств для одних и тех же обьектов.
        wb.find_element_by_name("firstname").clear()
        wb.find_element_by_name("firstname").send_keys(Contact.firstname)
        wb.find_element_by_name("middlename").clear()
        wb.find_element_by_name("middlename").send_keys(Contact.middlename)
        wb.find_element_by_name("lastname").clear()
        wb.find_element_by_name("lastname").send_keys(Contact.lastname)
        wb.find_element_by_name("nickname").clear()
        wb.find_element_by_name("nickname").send_keys(Contact.nickname)
        if Contact.photo is not "":
            wb.find_element_by_name("photo").send_keys(Contact.photo)
        wb.find_element_by_name("title").clear()
        wb.find_element_by_name("title").send_keys(Contact.title)
        wb.find_element_by_name("company").clear()
        wb.find_element_by_name("company").send_keys(Contact.company)
        wb.find_element_by_name("address").clear()
        wb.find_element_by_name("address").send_keys(Contact.address)
        wb.find_element_by_name("home").clear()
        wb.find_element_by_name("home").send_keys(Contact.address2)
        wb.find_element_by_name("mobile").clear()
        wb.find_element_by_name("mobile").send_keys(Contact.mobile)
        wb.find_element_by_name("work").clear()
        wb.find_element_by_name("work").send_keys(Contact.work)
        wb.find_element_by_name("fax").clear()
        wb.find_element_by_name("fax").send_keys(Contact.fax)
        wb.find_element_by_name("email").clear()
        wb.find_element_by_name("email").send_keys(Contact.email)
        wb.find_element_by_name("email2").clear()
        wb.find_element_by_name("email2").send_keys(Contact.email2)
        wb.find_element_by_name("email3").clear()
        wb.find_element_by_name("email3").send_keys(Contact.email3)
        wb.find_element_by_name("homepage").clear()
        wb.find_element_by_name("homepage").send_keys(Contact.homepage)
        # Fill fields with date
        # Обрабатываем случай, когда послали для выбора из списка пустое значение:
        if Contact.birthday_day is not "":
            Select(wb.find_element_by_name("bday")).select_by_visible_text(Contact.birthday_day)
        if Contact.birthday_month is not "":
            Select(wb.find_element_by_name("bmonth")).select_by_visible_text(Contact.birthday_month)
        wb.find_element_by_name("byear").clear()
        wb.find_element_by_name("byear").send_keys(Contact.birthday_year)
        if Contact.anniversary_day is not "":
            Select(wb.find_element_by_name("aday")).select_by_visible_text(Contact.anniversary_day)
        if Contact.anniversary_month is not "":
            Select(wb.find_element_by_name("amonth")).select_by_visible_text(Contact.anniversary_month)
        wb.find_element_by_name("ayear").clear()
        wb.find_element_by_name("ayear").send_keys(Contact.anniversary_year)
        wb.find_element_by_name("address2").clear()
        wb.find_element_by_name("address2").send_keys(Contact.address2)
        wb.find_element_by_name("phone2").clear()
        wb.find_element_by_name("phone2").send_keys(Contact.phone2)
        wb.find_element_by_name("notes").clear()
        wb.find_element_by_name("notes").send_keys(Contact.notes)
        # Submit contact editing
        wb.find_element_by_name("update").click()

    def delete_first(self):
        wb = self.app.wb
        wb.find_element_by_name("selected[]").click()
        wb.find_element_by_xpath("//input[@value='Delete']").click()
        WebDriverWait(wb, 5).until(EC.alert_is_present())
        Alert(wb).accept()
