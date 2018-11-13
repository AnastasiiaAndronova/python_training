
class Contact:

    def __init__(self, firstname, middlename, lastname, nickname, photo, title,
                 company, address, home, mobile, work, fax,
                 email, email2, email3, homepage, address2, phone2, notes,
                 birthday_day, birthday_month, birthday_year, anniversary_day, anniversary_month, anniversary_year):

        # form fields
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.photo = photo
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

