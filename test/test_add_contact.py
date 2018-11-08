# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
from fixture.application import Application


@ pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.open_home_page()
    app.session.login(user="admin", password="secret")
    app.contact.open_add_contact_page()
    app.contact.create(Contact(firstname="test first name", middlename="test middle name", lastname="test last name", nickname="test nick name",
                               title="test title", company="Test company", address="Test adress", home="Test home", mobile="Test mobile", work="Test work", fax="Test fax",
                               email="Test email", email2="Test email 2", email3="Test email 3", homepage="Test homepage", address2="Test address2", phone2="Test phone 2",
                               notes="Test notes", birthday_day = "1", birthday_month = "October", birthday_year = "1990", anniversary_day = "2", anniversary_month = "May", anniversary_year = "2000"))
    app.contact.return_to_home_page()
    app.session.logout()

def test_add_empty_contact(app):
    app.open_home_page()
    app.session.login(user="admin", password="secret")
    app.contact.open_add_contact_page()
    app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="",
                               title="", company="", address="", home="", mobile="", work="", fax="",
                               email="", email2="", email3="", homepage="", address2="", phone2="",
                               notes="", birthday_day = "", birthday_month="", birthday_year ="", anniversary_day="", anniversary_month="", anniversary_year=""))
    app.contact.return_to_home_page()
    app.session.logout()



