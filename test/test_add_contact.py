
from model.contact import Contact

def test_add_contact(app):
    app.contact.create(Contact(firstname="test first name",
                               middlename="test middle name",
                               lastname="test last name",
                               nickname="test nick name",
                               # photo="C:\\python_training\\Images\\image1.jpg",
                               title="test title",
                               company="Test company",
                               address="Test adress",
                               home="Test home",
                               mobile="Test mobile",
                               work="Test work", fax="Test fax",
                               email="Test email",
                               email2="Test email 2",
                               email3="Test email 3",
                               homepage="Test homepage",
                               address2="Test address2",
                               phone2="Test phone 2",
                               notes="Test notes",
                               birthday_day="1",
                               birthday_month="October",
                               birthday_year="1990",
                               anniversary_day="2",
                               anniversary_month="May",
                               anniversary_year="2000"))
    app.contact.open_homepage()


def test_add_empty_contact(app):
    app.contact.create(Contact())




