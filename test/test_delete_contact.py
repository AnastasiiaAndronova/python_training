from model.contact import Contact

def test_delete_first_contact(app):
    app.contact.open_homepage()
    if app.contact.count() == 0:
        app.contact.create(Contact())
    app.contact.delete_first()


