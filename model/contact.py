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
                 home=None,
                 mobile=None,
                 work=None,
                 fax=None,
                 email=None,
                 email2=None,
                 email3=None,
                 homepage=None,
                 address2=None,
                 phone2=None,
                 notes=None,
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
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.address2 = address2
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
        return "%s:%s:%s" % (self.id, self.lastname, self.firstname)

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

