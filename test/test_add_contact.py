# -*- coding: utf-8 -*-
from model.group_contact import Group_contact

def test_add_empty_contact(app):

    app.contact.create_contact(Group_contact(firstname ="", lastname="", homephone="", mobile="", email=""))

def test_add_contact(app):

    app.contact.create_contact(Group_contact(firstname="Anatolii", lastname="Zubov", homephone="222-22-22", mobile="846-743", email="gasgfg"))

