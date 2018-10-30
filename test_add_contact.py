# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from common_methods import login, logout, open_home_page
from forms_classes import Contact

import unittest

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wb = webdriver.Firefox()
        self.wb.implicitly_wait(30)
    
    def test_add_contact(self):
        wb = self.wb
        open_home_page(wb)
        login(wb, user="admin", password="secret")
        self.open_add_group_page(wb)
        self.create_new_contact(wb, Contact(firstname="test first name", middlename="test middle name",lastname="test last name",nickname="test nick name",title="test title",
            company="Test company", address="Test adress", home="Test home", mobile="Test mobile", work="Test work", fax="Test fax",
            email="Test email",email2="Test email 2",email3="Test email 3",homepage="Test homepage", address2 = "Test address2", phone2="Test phone 2", notes="Test notes"))
        self.return_to_home_page(wb)
        logout(wb)

    def return_to_home_page(self, wb):
        wb.find_element_by_link_text("home page").click()

    def create_new_contact(self, wb, Contact):
        # populate "add contact" fields

        wb.find_element_by_name("firstname").clear()
        wb.find_element_by_name("firstname").send_keys(Contact.firstname)
        wb.find_element_by_name("middlename").clear()
        wb.find_element_by_name("middlename").send_keys(Contact.middlename)
        wb.find_element_by_name("lastname").clear()
        wb.find_element_by_name("lastname").send_keys(Contact.lastname)
        wb.find_element_by_name("nickname").clear()
        wb.find_element_by_name("nickname").send_keys(Contact.nickname)
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

        Select(wb.find_element_by_name("bday")).select_by_visible_text("17")
        Select(wb.find_element_by_name("bmonth")).select_by_visible_text("October")
        wb.find_element_by_name("byear").clear()
        wb.find_element_by_name("byear").send_keys("1990")
        Select(wb.find_element_by_name("aday")).select_by_visible_text("1")
        Select(wb.find_element_by_name("amonth")).select_by_visible_text("December")

        wb.find_element_by_name("ayear").clear()
        wb.find_element_by_name("ayear").send_keys("2018")
        wb.find_element_by_name("address2").clear()
        wb.find_element_by_name("address2").send_keys(Contact.address2)
        wb.find_element_by_name("phone2").clear()
        wb.find_element_by_name("phone2").send_keys(Contact.phone2)
        wb.find_element_by_name("notes").clear()
        wb.find_element_by_name("notes").send_keys(Contact.notes)
        # Submit contact creation
        wb.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def open_add_group_page(self, wb):
        wb.find_element_by_link_text("add new").click()

    def tearDown(self):
        self.wb.quit()

if __name__ == "__main__":
    unittest.main()
