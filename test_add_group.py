# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from group import Group


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wb = webdriver.Firefox()
        self.wb.implicitly_wait(30)

    def test_add_group(self):
        wb = self.wb
        self.open_home_page(wb)
        self.login(wb, user="admin", password="secret")
        self.open_groups_page(wb)
        self.create_group(wb, Group(name="New test group", header="Test group header", footer="Test group footer"))
        self.return_to_groups_page(wb)
        self.logout(wb)

    def test_add_empty_group(self):
        wb = self.wb
        self.open_home_page(wb)
        self.login(wb, user="admin", password="secret")
        self.open_groups_page(wb)
        self.create_group(wb, Group(name="", header="", footer=""))
        self.return_to_groups_page(wb)
        self.logout(wb)

    def logout(self, wb):
        wb.find_element_by_link_text("Logout").click()

    def return_to_groups_page(self, wb):

        wb.find_element_by_link_text("group page").click()

    def create_group(self, wb, group):
        # start group creation
        wb.find_element_by_name("group_name").click()
        # populate group's form page
        wb.find_element_by_name("group_name").clear()
        wb.find_element_by_name("group_name").send_keys(group.name)
        wb.find_element_by_name("group_header").click()
        wb.find_element_by_name("group_header").clear()
        wb.find_element_by_name("group_header").send_keys(group.header)
        wb.find_element_by_name("group_footer").click()
        wb.find_element_by_name("group_footer").clear()
        wb.find_element_by_name("group_footer").send_keys(group.footer)
        # Submit group creation
        wb.find_element_by_name("submit").click()

    def open_groups_page(self, wb):
        wb.find_element_by_name("new").click()

    def login(self, wb, user, password):
        wb.find_element_by_name("user").clear()
        wb.find_element_by_name("user").send_keys(user)
        wb.find_element_by_id("LoginForm").click()
        wb.find_element_by_name("pass").click()
        wb.find_element_by_name("pass").clear()
        wb.find_element_by_name("pass").send_keys(password)
        wb.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wb):
        wb.get("http://localhost/addressbook/group.php")

    def tearDown(self):
        self.wb.quit()

if __name__ == "__main__":
    unittest.main()
