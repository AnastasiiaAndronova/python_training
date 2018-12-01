import re
from random import randrange
from model.contact import Contact


def test_some_contact_has_same_data_in_edit_and_home_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Let me be the first"))
    contacts = app.contact.get_contact_list()
    index = randrange(len(contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_all_emails_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.lastname == (contact_from_edit_page.lastname).strip()
    assert contact_from_home_page.firstname == (contact_from_edit_page.firstname).strip()
    assert contact_from_home_page.address == (contact_from_edit_page.address).strip()
    assert contact_from_home_page.id == contact_from_edit_page.id


# def test_phones_on_homepage_for_first_contact(app):
#     contact_from_home_page = app.contact.get_contact_list()[0]
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#     assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
#
# def test_phones_on_contact_view_page(app):
#     contact_from_view_page = app.contact.get_contact_from_view_page(0)
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#     assert contact_from_view_page.homephone == contact_from_edit_page.homephone
#     assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
#     assert contact_from_view_page.workphone == contact_from_edit_page.workphone
#     assert contact_from_view_page.phone2 == contact_from_edit_page.phone2


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                     map(lambda x: clear(x),
                        filter(lambda x: x is not None,
                         [contact.homephone,
                          contact.mobilephone,
                          contact.workphone,
                          contact.phone2]))))

def merge_all_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                     filter(lambda x: x is not None,
                         [contact.email,
                          contact.email2,
                          contact.email3])))