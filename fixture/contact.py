
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from model.contact import Contact
import re

class ContactHelper:

    def __init__(self, app):
        self.app = app

    contact_cache = None

    def return_to_homepage(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()
        WebDriverWait(wd, 5).until(EC.presence_of_element_located((By.NAME, "searchstring")))

    def open_homepage(self):
        wd = self.app.wd
# проверяем адрес урл и наличие поля для поиска, которое есть только на домашней странице (в списке контактов)
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name ("searchstring")) > 0):
            wd.find_element_by_link_text("home").click()

    def open_add_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("addressbook/edit.php") and len(wd.find_elements_by_name("submit")) > 0 and len(wd.find_elements_by_name("firstname"))):
            wd.find_element_by_link_text("add new").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_add_contact_page()
        self.fill_the_form(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.contact_cache = None

    def fill_the_form(self, contact):
        self.app.actions.change_field_value("firstname", contact.firstname)
        self.app.actions.change_field_value("middlename", contact.middlename)
        self.app.actions.change_field_value("lastname", contact.lastname)
        self.app.actions.change_field_value("nickname", contact.nickname)
        # if Contact.photo is not None:
        #     wd.find_element_by_name("photo").send_keys(Contact.photo)
        self.app.actions.change_field_value("title", contact.title)
        self.app.actions.change_field_value("company", contact.company)
        self.app.actions.change_field_value("address", contact.address)
        self.app.actions.change_field_value("address2", contact.address2)

        self.app.actions.change_field_value("home", contact.homephone)
        self.app.actions.change_field_value("mobile", contact.mobilephone)
        self.app.actions.change_field_value("work", contact.workphone)
        self.app.actions.change_field_value("fax", contact.faxphone)

        self.app.actions.change_field_value("email", contact.email)
        self.app.actions.change_field_value("email2", contact.email2)
        self.app.actions.change_field_value("email3", contact.email3)
        self.app.actions.change_field_value("homepage", contact.homepage)
        self.app.actions.select_in_dropdown("bday", contact.birthday_day)
        self.app.actions.change_field_value("byear", contact.birthday_year)
        self.app.actions.select_in_dropdown("bmonth", contact.birthday_month)
        self.app.actions.select_in_dropdown("aday", contact.anniversary_day)
        self.app.actions.select_in_dropdown("amonth", contact.anniversary_month)
        self.app.actions.change_field_value("ayear", contact.anniversary_year)
        self.app.actions.change_field_value("address2", contact.address2)
        self.app.actions.change_field_value("phone2", contact.phone2)
        self.app.actions.change_field_value("notes", contact.notes)

    def modify_first(self, contact):
        self.modify_by_index(index=0, contact=contact)

    def modify_by_index(self, contact, index):
        wd = self.app.wd
        self.app.contact.open_homepage()
        self.open_for_edit_by_index(index)
        self.fill_the_form(contact)
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def open_for_edit_by_index(self, index):
        wd = self.app.wd
        self.open_homepage()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def delete_first(self):
        self.delete_by_index(0)

    def delete_by_index(self, index):
        wd = self.app.wd
        self.app.contact.open_homepage()
        self.select_by_index(index)
        wd.find_element_by_css_selector("input[value=Delete]").click()
        WebDriverWait(wd, 3).until(EC.alert_is_present())
        wd.switch_to.alert.accept()
        WebDriverWait(wd, 3).until(EC.presence_of_element_located((By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Record successful deleted'])[1]/preceding::h1[1]")))
        self.contact_cache = None

    def select_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def count(self):
        wd = self.app.wd
        self.open_homepage()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_homepage()
            self.contact_cache = []
            for i in wd.find_elements_by_css_selector("tr[name=entry]"):
                cells = i.find_elements_by_tag_name("td")
                lastname=cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                id = i.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(lastname=lastname,
                                                  firstname=firstname,
                                                  id=id,
                                                  address=address,
                                                  all_phones_from_home_page=all_phones,
                                                  all_emails_from_home_page=all_emails
                                                  )
                                        )
        return list(self.contact_cache)

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_homepage()
        # wd.find_elements_by_css_selector('img[alt="Details"]')[index].click()
        # WebDriverWait(wd, 3).until(EC.presence_of_element_located((By.NAME, "modifiy")))
        # wd.find_element_by_name("modifiy")
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()
        WebDriverWait(wd, 3).until(EC.presence_of_element_located((By.NAME, "modifiy")))


    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_for_edit_by_index(index)
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        #phones
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        #emails
        email1 = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")

        return Contact(firstname=firstname,
                       lastname=lastname,
                       address=address,
                       homephone=homephone,
                       mobilephone=mobilephone,
                       workphone=workphone,
                       phone2=phone2,
                       email = email1,
                       email2 =email2,
                       email3 = email3,
                       id=id)


    # nickname = wd.find_element_by_name("nickname").get_attribute("value")
    # title = wd.find_element_by_name("title").get_attribute("value")
    # company = wd.find_element_by_name("company").get_attribute("value")


    # homepage = wd.find_element_by_name("homepage").get_attribute("value")
    # address2 = wd.find_element_by_name("address2").get_attribute("value")
    # phone2 = wd.find_element_by_name("phone2").get_attribute("value")
    # notes = wd.find_element_by_name("notes").get_attribute("value")
    #
    # # Dates (Redo later)
    # birthday_day = wd.find_element_by_name("birthday_day").get_attribute("value")
    # birthday_month = wd.find_element_by_name("birthday_month").get_attribute("value")
    # birthday_year = wd.find_element_by_name("birthday_year").get_attribute("value")
    # anniversary_day = wd.find_element_by_name("anniversary_day").get_attribute("value")
    # anniversary_month = wd.find_element_by_name("anniversary_month").get_attribute("value")
    # anniversary_year = wd.find_element_by_name("anniversary_year").get_attribute("value")

    # Mobile phones

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id('content').text
        homephone = self.app.actions.search_matching_by_template('H: (.*)', text)
        workphone = self.app.actions.search_matching_by_template("W: (.*)", text)
        mobilephone = self.app.actions.search_matching_by_template("M: (.*)", text)
        phone2 = self.app.actions.search_matching_by_template("P: (.*)", text)
        return Contact(homephone=homephone,
                       mobilephone=mobilephone,
                       workphone=workphone,
                       phone2=phone2)




