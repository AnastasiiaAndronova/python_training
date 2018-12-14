from model.contact import Contact
import re

def clear(string):
    return re.sub("[\n() .]","",string)

def test_check_contact(app,db):
    app.contact.open_homepage()
    db_contact=db.get_full_contact_list()
    ap_contact=app.contact.get_contact_list()
    #проверяем на  колличество записей
    db_len=len (db_contact)
    ap_len=len (ap_contact)
    assert db_len == ap_len
    def clean(contact):
        return Contact(id=contact.id, firstname=contact.firstname.strip(), lastname=contact.lastname.strip())
    #проверка с использованием старого метода сравнения
    assert sorted(map(clean, db.get_contact_list()), key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    count_len=0
    for i in db_contact:
        for m in ap_contact:
            if i.id==m.id:
                assert clear(i.all_phones_from_home_page) ==clear(m.all_phones_from_home_page)
                assert clear(i.all_emails_from_home_page) == clear(m.all_emails_from_home_page)
                assert i.lastname.strip() ==  m.lastname.strip()
                assert i.firstname.strip() == m.firstname.strip()
                assert clear(i.address) == clear(m.address)
                count_len+=1

    # проверим, что количество найденных пар совпадает с колличеством записей (все записи просмотрены, нет лишних и не совпадающих по ID)
    assert db_len == count_len



