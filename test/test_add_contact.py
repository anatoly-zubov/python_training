# -*- coding: utf-8 -*-
import pytest
from model.group_contact import Group_contact
from fixture.appcontact import Appcontact

@pytest.fixture
def app(request):
    fixture = Appcontact()
    request.addfinalizer(fixture.destroy)
    return fixture

def untitled_test_case(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_contact(Group_contact(firstname ="", lastname="", homephone="", mobile="", email=""))
    app.session.logout()

def test_untitled_test_case(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_contact(Group_contact(firstname="Anatolii", lastname="Zubov", homephone="222-22-22", mobile="846-743", email="gasgfg"))
    app.session.logout()
