# -*- coding: utf-8 -*-
from model.group_contact import Group_contact

"""
def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Group_contact(firstname="", lastname="", mobile="", email="")
    app.contact.create_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Group_contact.id_or_max) == sorted(new_contacts, key=Group_contact.id_or_max)
"""


def test_add_contact(app):
    contact = Group_contact(firstname="Anatolii", lastname="Zhukov", mobile="846-743", email="gasgfg")
    old_contacts = app.contact.get_contact_list()
    app.contact.create_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Group_contact.id_or_max) == sorted(new_contacts, key=Group_contact.id_or_max)
