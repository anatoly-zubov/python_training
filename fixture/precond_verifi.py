from model.group import Group
from model.group_contact import Group_contact


def precond_verifi_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))

def precond_verifi_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Group_contact(firstname="Name"))
