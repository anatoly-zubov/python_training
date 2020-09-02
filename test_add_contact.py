# -*- coding: utf-8 -*-

import pytest
from group_contact import Group_contact
from Appcontact import Appcontact


@pytest.fixture
def app(request):
    fixture = Appcontact()
    request.addfinalizer(fixture.destroy)
    return Appcontact

def add_empty_contact(app):
    app.open_home_page()
    app.login("admin", "secret")
    app.create_contact(Group_contact(firstname="", lastname="", homephone="", mobile="", email=""))
    app.return_home_page()
    app.logout()

def test_untitled_test_case(app):
    app.open_home_page()
    app.login("admin", "secret")
    app.create_contact(
        Group_contact(firstname="Anatolii", lastname="Zubov", homephone="222-22-22", mobile="846-743-82-13",
                          email="gagfg\\dsgfg"))
    app.return_home_page()
    app.logout()
