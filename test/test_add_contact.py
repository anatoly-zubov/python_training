# -*- coding: utf-8 -*-
import pytest
from model.group_contact import Group_contact
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_contact(Group_contact(firstname ="", lastname="", homephone="", mobile="", email=""))
    app.session.logout()

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_contact(Group_contact(firstname="Anatolii", lastname="Zubov", homephone="222-22-22", mobile="846-743", email="gasgfg"))
    app.session.logout()
