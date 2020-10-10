# -*- coding: utf-8 -*-
from model.group_contact import Group_contact
import pytest
import random
import string

def random_string(prefix,maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range (random.randrange(maxlen))])

testdata = [Group_contact(firstname="", lastname="", mobile="", email="")] + [
    Group_contact(firstname=random_string("firstname", 8), lastname=random_string("lastname", 6),
                  mobile=random_string("mobile", 10),email=random_string("email", 10))
    for i in range (5)
]
@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app,contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Group_contact.id_or_max) == sorted(new_contacts, key=Group_contact.id_or_max)
