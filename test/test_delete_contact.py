from model.contact import Contact

def test_delete_first_contact(app):
    app.contact.open_homepage()
    if app.contact.count() == 0:
        app.contact.create(Contact())
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first()
    new_conctacts = app.contact.get_contact_list()
    assert len(old_contacts) -1 == len(new_conctacts)
    old_contacts[0:1]=[]
    assert old_contacts == new_conctacts

