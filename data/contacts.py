import random
import string
from model.group_contact import Group_contact


testdata = [
    Group_contact(firstname="firstname1", lastname="lastname1", mobile="11111111", email="email1"),
    Group_contact(firstname="firstname2", lastname="lastname2", mobile="22222222", email="email2")
]
"""
def random_string(prefix,maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range (random.randrange(maxlen))])

testdata = [Group_contact(firstname="", lastname="", mobile="", email="")] + [
    Group_contact(firstname=random_string("firstname", 8), lastname=random_string("lastname", 6),
                  mobile=random_string("mobile", 10),email=random_string("email", 10))
    for i in range (5)
]
"""