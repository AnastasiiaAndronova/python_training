# класс с методами для взаимодействия с элементами (заполнять поля, выбирать значение из списка и т.п. которые будут встречаться во многих местах)
from selenium.webdriver.support.ui import Select
class ActionsHelper:

    def __init__(self,app):
        self.app = app

    def change_field_value(self,field_name,text=None):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).send_keys(text)

    def select_in_dropdown(self, list_name, list_value=None):
        wd = self.app.wd
        if list_value is not None:
            Select(wd.find_element_by_name(list_name)).select_by_visible_text(list_value)
