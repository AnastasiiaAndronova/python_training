import random
import string
import re
import os.path
import jsonpickle
import getopt
import sys
from model.contact import Contact;


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file="])
except getopt.GetoptError as err:
    print(err)
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contact.json"

for o, a in opts:
   if o == "-n":
       n = int(a)
   elif o == "-f":
       f = a
from model.contact import Contact
import random
import string
import re


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
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
                      anniversary_year=str(random.randint(1950, 2000))) for x in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",f)
with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))

