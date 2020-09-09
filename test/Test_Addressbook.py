# -*- coding: utf-8 -*-
from model.group import Group

def test_empty_add_group(app):
    app.group.create(Group(name="", header="", footer=""))
    
def test_add_group(app):
    app.group.create(Group(name="newgroup", header="grouplogo", footer="groupfooter"))


