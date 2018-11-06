from selenium import webdriver
from selenium.webdriver.support.ui import Select
from group import Group
from contact import Contact

class Application:

    def __init__(self):
        self.wb = webdriver.Firefox()
        self.wb.implicitly_wait(30)

    def destroy(self):
        self.wb.quit()

    def login(self, user, password):
        wb = self.wb
        wb.find_element_by_name("user").clear()
        wb.find_element_by_name("user").send_keys(user)
        wb.find_element_by_id("LoginForm").click()
        wb.find_element_by_name("pass").click()
        wb.find_element_by_name("pass").clear()
        wb.find_element_by_name("pass").send_keys(password)
        wb.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        wb = self.wb
        wb.find_element_by_link_text("Logout").click()

    def open_groups_page(self):
        wb = self.wb
        wb.find_element_by_link_text("groups").click()

    def open_add_group_page(self):
        wb = self.wb
        wb.find_element_by_name("new").click()

    def open_add_contact_page(self):
        wb = self.wb
        wb.find_element_by_link_text("add new").click()

    def return_to_groups_page(self):
        wb = self.wb
        wb.find_element_by_link_text("group page").click()

    def return_to_home_page(self):
        wb = self.wb
        wb.find_element_by_link_text("home page").click()

    def open_home_page(self):
        wb = self.wb
        wb.get("http://localhost/addressbook/")

    # def open_home_page(self):
    #     wb = self.wb
    #     wb.get("http://localhost/addressbook/group.php")

    def create_new_contact(self, Contact):
        wb = self.wb
        # populate "add contact" fields
        # Хотелось сделать универсальный метод populate_form_fields но пока непонятно как лучше "правильно" хранить множество свойств для одних и тех же обьектов.
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
        # Fill fields with date

        # Обрабатываем случай, когда послали для выбора из списка пустое значение:
        # это скорее всего не очень хорошее решение, но в конкретно нашем случае тесты работоспособны
        if Contact.birthday_day is not "":
            Select(wb.find_element_by_name("bday")).select_by_visible_text(Contact.birthday_day)
        if Contact.birthday_month is not "":
            Select(wb.find_element_by_name("bmonth")).select_by_visible_text(Contact.birthday_month)
        wb.find_element_by_name("byear").clear()
        wb.find_element_by_name("byear").send_keys(Contact.birthday_year)
        if Contact.anniversary_day is not "":
            Select(wb.find_element_by_name("aday")).select_by_visible_text(Contact.anniversary_day)
        if Contact.anniversary_month is not "":
            Select(wb.find_element_by_name("amonth")).select_by_visible_text(Contact.anniversary_month)
        wb.find_element_by_name("ayear").clear()
        wb.find_element_by_name("ayear").send_keys(Contact.anniversary_year)

        wb.find_element_by_name("address2").clear()
        wb.find_element_by_name("address2").send_keys(Contact.address2)
        wb.find_element_by_name("phone2").clear()
        wb.find_element_by_name("phone2").send_keys(Contact.phone2)
        wb.find_element_by_name("notes").clear()
        wb.find_element_by_name("notes").send_keys(Contact.notes)
        # Submit contact creation
        wb.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def create_group(self,group):
        wb = self.wb
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





