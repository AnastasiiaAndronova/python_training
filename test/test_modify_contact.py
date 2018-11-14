from model.contact import Contact
# пока редактируем весь контакт целиком, но уже можем редактировать так же и частями
def test_modify_first_contact(app):
    app.session.login(user="admin", password="secret")
    app.contact.modify_first(Contact(firstname="test first name1",
                                     middlename="test middle name1",
                                     lastname="test last name1",
                                     nickname="test nick name1",
                                     photo="C:\\python_training\\Images\\image2.jpg",
                                     title="test title1",
                                     company="Test company1",
                                     address="Test adress1",
                                     home="Test home2",
                                     mobile="Test mobile1",
                                     work="Test work1",
                                     fax="Test fax1",
                                     email="Test email1",
                                     email2="Test email 21",
                                     email3="Test email 31",
                                     homepage="Test homepage1",
                                     address2="Test address21",
                                     phone2="Test phone 21",
                                     notes="Test notes1",
                                     birthday_day="11",
                                     birthday_month="September",
                                     birthday_year="1991",
                                     anniversary_day="3",
                                     anniversary_month="August",
                                     anniversary_year="2018"))
    app.contact.return_to_home_page()
    app.session.logout()
# пока что только первая группа