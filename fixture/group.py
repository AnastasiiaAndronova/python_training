from model.group import Group
import string

class GroupHelper:

    def __init__(self, app):
        self.app = app

    group_cache = None

    def open_groups_page(self):
        wd = self.app.wd
# проверяем адрес урл и наличие кнопки создания новой группы
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def open_add_group_page(self):
        wd = self.app.wd
# проверяем адрес урл и наличие элемента с именем group name который должен там быть... но он есть еще на странице редактирования группы.
# поэтому проверяем так же кнопку enter information , которая есть в форме создания и нет в форме редактирования
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("group_name")) > 0 and len(wd.find_elements_by_name("submit")) > 0):
            wd.find_element_by_link_text("groups").click()
            wd.find_element_by_name("new").click()

    def return_to_groups_page(self):
# А в этом случае тест пройдет и даже не поргуается на отсутствие этой кнопки, что тоже не хорошо
        wd = self.app.wd
        if not len(wd.find_elements_by_link_text("group page")) > 0:
            return
        wd.find_element_by_link_text("group page").click()

    def create(self, group):
        wd = self.app.wd
        self.open_add_group_page()
        self.fill_the_form(group)
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()
        self.group_cache = None

    def fill_the_form(self, group):
        self.app.actions.change_field_value("group_name", group.name)
        self.app.actions.change_field_value("group_header", group.header)
        self.app.actions.change_field_value("group_footer", group.footer)

    def edit_first(self, group):
        wd = self.app.wd
        self.select_by_index(0)
        wd.find_element_by_name("edit").click()
        self.fill_the_form(group)
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def edit_some_group(self, group, index):
        wd = self.app.wd
        self.select_by_index(index)
        wd.find_element_by_name("edit").click()
        self.fill_the_form(group)
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def select_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_by_index (self, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_by_index(index)
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def delete_first (self):
        self.delete_by_index(0)

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)




