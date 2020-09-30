from random import randrange
from model.group_contact import Group_contact
from fixture.precond_verifi import precond_verifi_contact


def test_modify_contact_firstname(app):
    precond_verifi_contact(app)
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Group_contact(lastname="New_Name")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(contact,index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Group_contact.id_or_max) == sorted(new_contacts, key=Group_contact.id_or_max)
