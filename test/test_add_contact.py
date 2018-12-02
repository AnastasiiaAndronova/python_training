from model.contact import Contact
import pytest
import random
import string
import re


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + re.sub("'", " ", string.punctuation) + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
testdata =[Contact()] + [Contact(firstname=random_string("firstname", 20),
                      middlename=random_string("middlename",20),
                      lastname=random_string("lastname", 20),
                      nickname=random_string("nickname",20),
                      title=random_string("title", 20),
                      company=random_string("company", 20),
                      address=random_string("address", 40),
                      homephone=random_string("homephone",10),
                      mobilephone=random_string("mobilephone", 10),
                      workphone=random_string("workphone", 10),
                      phone2=random_string("phone2", 10),
                      faxphone=random_string("faxphone", 10),
                      email=random_string("email", 30),
                      email2=random_string("email2",30),
                      email3=random_string("email3", 30),
                      homepage=random_string("homepage", 30),
                      address2=random_string("address2", 40),
                      notes=random_string("notes", 40),
                      home =random_string("home", 10),
                      birthday_day= str(random.randint(1, 28)),
                      birthday_month=months[random.randint(0,11)],
                      birthday_year=str(random.randint(1950, 2000)),
                      anniversary_day=str(random.randint(1, 28)),
                      anniversary_month=months[random.randint(0,11)],
                      anniversary_year=str(random.randint(1950, 2000))) for x in range(5)]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])

def test_add_contact(app, contact):


    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    app.contact.return_to_homepage()
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    new_contacts.append(contact)
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



# def test_add_empty_contact(app):
#     contact = Contact()
#     old_contacts = app.contact.get_contact_list()
#     app.contact.create(contact)
#     app.contact.return_to_homepage()
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) + 1 == len(new_contacts)
#     new_contacts.append(contact)
#     assert sorted(new_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)




