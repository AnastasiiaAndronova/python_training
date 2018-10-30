# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from common_methods import login,logout,open_home_page

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
        self.create_new_contact(wb)
        self.return_to_home_page(wb)
        logout(wb)

    def return_to_home_page(self, wb):
        wb.find_element_by_link_text("home page").click()

    def create_new_contact(self, wb):
        wb.find_element_by_name("firstname").click()
        wb.find_element_by_name("firstname").clear()
        wb.find_element_by_name("firstname").send_keys("5555")
        wb.find_element_by_name("middlename").click()
        wb.find_element_by_name("middlename").clear()
        wb.find_element_by_name("middlename").send_keys("5555")
        wb.find_element_by_name("lastname").click()
        wb.find_element_by_name("lastname").clear()
        wb.find_element_by_name("lastname").send_keys("5555")
        wb.find_element_by_name("nickname").click()
        wb.find_element_by_name("nickname").clear()
        wb.find_element_by_name("nickname").send_keys("5333")
        wb.find_element_by_name("title").click()
        wb.find_element_by_name("title").click()
        wb.find_element_by_name("title").clear()
        wb.find_element_by_name("title").send_keys("3333")
        wb.find_element_by_name("company").click()
        wb.find_element_by_name("company").clear()
        wb.find_element_by_name("company").send_keys("rrrr")
        wb.find_element_by_name("address").click()
        wb.find_element_by_name("address").clear()
        wb.find_element_by_name("address").send_keys("rrrr")
        wb.find_element_by_name("home").click()
        wb.find_element_by_name("home").clear()
        wb.find_element_by_name("home").send_keys("rrrr")
        wb.find_element_by_name("mobile").click()
        wb.find_element_by_name("mobile").clear()
        wb.find_element_by_name("mobile").send_keys("yyy")
        wb.find_element_by_name("work").click()
        wb.find_element_by_name("work").clear()
        wb.find_element_by_name("work").send_keys("rrr")
        wb.find_element_by_name("fax").click()
        wb.find_element_by_name("fax").clear()
        wb.find_element_by_name("fax").send_keys("tttt")
        wb.find_element_by_name("email").click()
        wb.find_element_by_name("email").clear()
        wb.find_element_by_name("email").send_keys("eeee")
        wb.find_element_by_name("email2").click()
        wb.find_element_by_name("email2").clear()
        wb.find_element_by_name("email2").send_keys("eeee")
        wb.find_element_by_name("email3").click()
        wb.find_element_by_name("email3").clear()
        wb.find_element_by_name("email3").send_keys("tttt")
        wb.find_element_by_name("homepage").click()
        wb.find_element_by_name("homepage").clear()
        wb.find_element_by_name("homepage").send_keys("tttt")
        wb.find_element_by_name("bday").click()
        Select(wb.find_element_by_name("bday")).select_by_visible_text("17")
        wb.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Birthday:'])[1]/following::option[19]").click()
        wb.find_element_by_name("bmonth").click()
        Select(wb.find_element_by_name("bmonth")).select_by_visible_text("October")
        wb.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Birthday:'])[1]/following::option[44]").click()
        wb.find_element_by_name("byear").click()
        wb.find_element_by_name("byear").clear()
        wb.find_element_by_name("byear").send_keys("1990")
        wb.find_element_by_name("aday").click()
        Select(wb.find_element_by_name("aday")).select_by_visible_text("1")
        wb.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Anniversary:'])[1]/following::option[3]").click()
        wb.find_element_by_name("amonth").click()
        Select(wb.find_element_by_name("amonth")).select_by_visible_text("December")
        wb.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Anniversary:'])[1]/following::option[46]").click()
        wb.find_element_by_name("ayear").click()
        wb.find_element_by_name("ayear").clear()
        wb.find_element_by_name("ayear").send_keys("2018")
        wb.find_element_by_name("address2").click()
        wb.find_element_by_name("address2").clear()
        wb.find_element_by_name("address2").send_keys("tttt")
        wb.find_element_by_name("phone2").click()
        wb.find_element_by_name("phone2").clear()
        wb.find_element_by_name("phone2").send_keys("tttt")
        wb.find_element_by_name("notes").click()
        wb.find_element_by_name("notes").clear()
        wb.find_element_by_name("notes").send_keys("3333")
        # Submit contact creation
        wb.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def open_add_group_page(self, wb):
        wb.find_element_by_link_text("add new").click()

    def tearDown(self):
        self.wb.quit()

if __name__ == "__main__":
    unittest.main()
