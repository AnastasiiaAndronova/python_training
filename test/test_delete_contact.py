from model.contact import Contact
from random import randrange
import random
def test_delete_first_contact(app):
    app.contact.open_homepage()
    if app.contact.count() == 0:
        app.contact.create(Contact())
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first()
    assert len(old_contacts) - 1 == app.contact.count()
    new_conctacts = app.contact.get_contact_list()
    old_contacts[0:1]=[]
    assert old_contacts == new_conctacts


def test_delete_some_contact_old(app):
    app.contact.open_homepage()
    if app.contact.count() == 0:
        app.contact.create(Contact())
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_conctacts = app.contact.get_contact_list()
    old_contacts[index:index+1]=[]
    assert old_contacts == new_conctacts


def test_delete_some_contact(app,db,check_ui):
    app.contact.open_homepage()
    if len (db.get_contact_list()) == 0:
        app.contact.create(Contact())
    old_contacts = db.get_contact_list()
    delete_contact = random.choice(old_contacts)
    app.contact.delete_by_id(delete_contact.id)
    assert len(old_contacts) - 1 == len(db.get_contact_list())
    if check_ui:
        def clean(contact):
            return Contact(id=contact.id, firstname=contact.firstname.strip(),lastname=contact.lastname.strip())
        assert sorted(map(clean,db.get_contact_list()),key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),key=Contact.id_or_max)


