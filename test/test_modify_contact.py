from model.contact import Contact
from random import randrange
# пока редактируем весь контакт целиком, но уже можем редактировать так же и частями
def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact())
    app.contact.open_homepage()
    old_contacts = app.contact.get_contact_list()
    contact = (Contact(firstname="test first name1", lastname="test last name1"))
    contact.id = old_contacts[0].id
    app.contact.modify_first(contact)
    assert len(old_contacts) == app.contact.count()
    new_conctacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_conctacts, key=Contact.id_or_max)

def test_modify_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact())
    app.contact.open_homepage()
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = (Contact(firstname="test first name1", lastname="test last name1"))
    contact.id = old_contacts[index].id
    app.contact.modify_by_index(contact, index)
    assert len(old_contacts) == app.contact.count()
    new_conctacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_conctacts, key=Contact.id_or_max)

    # app.contact.modify_first(Contact(firstname="test first name1",
    #                                  middlename="test middle name1",
    #                                  lastname="test last name1",
    #                                  nickname="test nick name1",
    #                                  # photo="C:\\python_training\\Images\\image2.jpg",
    #                                  title="test title1",
    #                                  company="Test company1",
    #                                  address="Test adress1",
    #                                  home="Test home2",
    #                                  mobile="Test mobile1",
    #                                  work="Test work1",
    #                                  fax="Test fax1",
    #                                  email="Test email1",
    #                                  email2="Test email 21",
    #                                  email3="Test email 31",
    #                                  homepage="Test homepage1",
    #                                  address2="Test address21",
    #                                  phone2="Test phone 21",
    #                                  notes="Test notes1",
    #                                  birthday_day="11",
    #                                  birthday_month="September",
    #                                  birthday_year="1991",
    #                                  anniversary_day="3",
    #                                  anniversary_month="August",
    #                                  anniversary_year="2018"))