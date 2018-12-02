from sys import maxsize

class Contact:

    def __init__(self,
                 firstname=None,
                 middlename=None,
                 lastname=None,
                 nickname=None,
                 # photo=None,
                 title=None,
                 company=None,
                 address=None,
                 all_phones_from_home_page=None,
                 homephone=None,
                 mobilephone=None,
                 workphone=None,
                 faxphone=None,
                 email=None,
                 email2=None,
                 email3=None,
                 all_emails_from_home_page = None,
                 homepage=None,
                 address2=None,
                 phone2=None,
                 notes=None,
                 home = None,
                 birthday_day=None,
                 birthday_month=None,
                 birthday_year=None,
                 anniversary_day=None,
                 anniversary_month=None,
                 anniversary_year=None,
                 id = None):

        # form fields
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        # self.photo = photo
        self.title = title
        self.company = company
        self.address = address

        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.faxphone = faxphone

        self.all_phones_from_home_page = all_phones_from_home_page

        self.email = email
        self.email2 = email2
        self.email3 = email3

        self.all_emails_from_home_page = all_emails_from_home_page
        self.homepage = homepage
        self.address2 = address2
        self.home = home
        self.phone2 = phone2
        self.notes = notes
        # For dates:
        self.birthday_day = birthday_day
        self.birthday_month = birthday_month
        self.birthday_year = birthday_year
        self.anniversary_day = anniversary_day
        self.anniversary_month = anniversary_month
        self.anniversary_year = anniversary_year

        self.id = id

# метод определяет как будут выглядеть обьекты при выводе на консоль
    def __repr__(self):
        return "id = %s:, lastname = %s: firstname = %s: middlename = %s: nickname = %s: " \
               "title = %s: company = %s: address =  %s: " \
               "homephone = %s: mobilephone = %s: workphine = %s: faxphone = %s:" \
               " email = %s: email2 = %s: email3 = %s: address2 = %s: " \
               "phone2 = %s: notes = %s: birthday = %s: bmonth = %s:" \
               " byear = %s: anday = %s: anmonth = %s: anyear = %s:%s" % (
            self.id,
            self.lastname,
            self.firstname,
            self.middlename,
            self.nickname,
            self.title,
            self.company,
            self.address,
            self.homephone,
            self.mobilephone,
            self.workphone,
            self.faxphone,
            self.email,
            self.email2,
            self.email3,
            self.address2,
            self.phone2,
            self.notes,
            self.home,
            self.birthday_day,
            self.birthday_month,
            self.birthday_year,
            self.anniversary_day,
            self.anniversary_month,
            self.anniversary_year
        )

# метод сравнения

    def __eq__(self, other):

        if self.lastname != other.lastname:
            return False

        elif self.firstname != other.firstname:
            return False

        elif self.id is not None and other.id is not None and self.id != other.id:
            return False

        return True

    def id_or_max(self):
        if self.id:
            return int(self.id)
        return maxsize

