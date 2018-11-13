class GroupHelper:

    def __init__(self, app):
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
        self.app.actions.change_field_value("group_name", group.name)
        self.app.actions.change_field_value("group_header", group.header)
        self.app.actions.change_field_value("group_footer", group.footer)
        # Submit group creation
        wb.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def edit_first(self, group):
        wb = self.app.wb
        # start group editing
        self.select_first()
        wb.find_element_by_name("edit").click()
        # populate group's form page
        self.app.actions.change_field_value("group_name", group.name)
        self.app.actions.change_field_value("group_header", group.header)
        self.app.actions.change_field_value("group_footer", group.footer)
        # Submit group creation
        wb.find_element_by_name("update").click()
        self.return_to_groups_page()

    def select_first(self):
        wb = self.app.wb
        wb.find_element_by_name("selected[]").click()

    def delete_first (self):
        wb = self.app.wb
        self.open_groups_page()
        wb.find_element_by_name("selected[]").click()
        wb.find_element_by_name("delete").click()
        self.return_to_groups_page()
