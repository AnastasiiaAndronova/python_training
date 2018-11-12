
def test_delete_first_contact(app):
    app.session.login(user="admin", password="secret")
    app.contact.delete_first()
    app.session.logout()

# some test comment
# пока что только первый контакт