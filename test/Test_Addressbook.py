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
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
    
def test_addressbook(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="newgroup", header="grouplogo", footer="groupfooter"))
    app.session.logout()

