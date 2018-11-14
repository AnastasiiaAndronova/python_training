
def test_delete_first_contact(app):
    app.session.login()
    app.contact.delete_first()
    app.contact.navigate_to_home_page()
    app.session.logout()

# some test comment
# пока что только первый контакт