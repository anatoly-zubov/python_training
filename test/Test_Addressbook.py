# -*- coding: utf-8 -*-
from model.group import Group

def test_empty_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
    
def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="newgroup", header="grouplogo", footer="groupfooter"))
    app.session.logout()

