
class GroupHelper:

    def __init__(self,app):
        self.app = app

    def open_groups_page(self):
        wb = self.app.wb
        wb.find_element_by_link_text("groups").click()

    def open_add_group_page(self):
        wb = self.app.wb
        wb.find_element_by_name("new").click()

    def open_add_contact_page(self):
        wb = self.app.wb
        wb.find_element_by_link_text("add new").click()

    def return_to_groups_page(self):
        wb = self.app.wb
        wb.find_element_by_link_text("group page").click()

    def create(self,group):
        wb = self.app.wb
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
