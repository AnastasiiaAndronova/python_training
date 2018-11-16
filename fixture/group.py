class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def open_add_group_page(self):
        wd = self.app.wd
        wd.find_element_by_name("new").click()

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def create(self,group):
        wd = self.app.wd
        # start group creationf
        self.open_add_group_page()
        self.fill_the_form(group)
        # Submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def fill_the_form(self, group):
        self.app.actions.change_field_value("group_name", group.name)
        self.app.actions.change_field_value("group_header", group.header)
        self.app.actions.change_field_value("group_footer", group.footer)

    def edit_first(self, group):
        wd = self.app.wd
        # start group editing
        self.select_first()
        wd.find_element_by_name("edit").click()
        # populate group's form page
        self.fill_the_form(group)
        # Submit group creation
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()

    def select_first(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def delete_first (self):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
