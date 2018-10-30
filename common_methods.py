

def login(wb, user, password):
    wb.find_element_by_name("user").clear()
    wb.find_element_by_name("user").send_keys(user)
    wb.find_element_by_id("LoginForm").click()
    wb.find_element_by_name("pass").click()
    wb.find_element_by_name("pass").clear()
    wb.find_element_by_name("pass").send_keys(password)
    wb.find_element_by_xpath("//input[@value='Login']").click()

def open_home_page(wb):
    wb.get("http://localhost/addressbook/")

def logout(wb):
        wb.find_element_by_link_text("Logout").click()
