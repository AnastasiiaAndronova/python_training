import random
import string
import re
from model.group import Group


testdata = [
    Group(name="name1", header="name1", footer="footer1"),
    Group(name="name2", header="name2", footer="footer2")
]
# def random_string(prefix, maxlen):
#     symbols = string.ascii_letters + string.digits + re.sub("'", " ", string.punctuation) + " "*10
#     return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
#
# testdata = [Group(name="", header='', footer='')] + \
#            [
#         Group(name=name, header=header,footer = footer)
#         for name in ["", random_string("name", 10)]
#         for header in ["", random_string("header", 20)]
#         for footer in ["", random_string("footer", 20)]
#            ]

