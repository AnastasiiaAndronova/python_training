# класс с методами для взаимодействия с элементами (заполнять поля, выбирать значение из списка и т.п. которые будут встречаться во многих местах)
from selenium.webdriver.support.ui import Select
class ActionsHelper:

    def __init__(self,app):
        self.app = app

    def change_field_value(self,field_name,text=None):
        wb = self.app.wb
        if text is not None:
            wb.find_element_by_name(field_name).clear()
            wb.find_element_by_name(field_name).click()
            wb.find_element_by_name(field_name).send_keys(text)

    def select_in_dropdown(self, list_name, list_value=None):
        wb = self.app.wb
        if list_value is not None:
            Select(wb.find_element_by_name(list_name)).select_by_visible_text(list_value)
