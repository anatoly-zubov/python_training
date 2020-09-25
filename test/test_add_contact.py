# -*- coding: utf-8 -*-
from model.group_contact import Group_contact

def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create_contact(Group_contact(firstname ="", lastname="", mobile="", email=""))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)

def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create_contact(Group_contact(firstname="Anatolii", lastname="Zubov", mobile="846-743", email="gasgfg"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)

