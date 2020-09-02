# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_empty_addressbook(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()
    
def test_addressbook(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="newgroup", header="grouplogo", footer="groupfooter"))
    app.logout()

