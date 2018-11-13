
class GroupHelper:

    def __init__(self,app):
        self.app = app

    def open_groups_page(self):
        wb = self.app.wb
        wb.find_element_by_link_text("groups").click()

    def open_add_group_page(self):
        wb = self.app.wb
        wb.find_element_by_name("new").click()

    def return_to_groups_page(self):
        wb = self.app.wb
        wb.find_element_by_link_text("group page").click()

    def create(self,group):
        wb = self.app.wb
        # start group creation
        self.open_add_group_page()
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
        self.return_to_groups_page()

    def edit_first(self, group):
        wb = self.app.wb
        # start group editing
        wb.find_element_by_name("selected[]").click()
        wb.find_element_by_name("edit").click()
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
        wb.find_element_by_name("update").click()
        self.return_to_groups_page()

    def delete_first (self):
        wb = self.app.wb
        self.open_groups_page()
        wb.find_element_by_name("selected[]").click()
        wb.find_element_by_name("delete").click()
        self.return_to_groups_page()
