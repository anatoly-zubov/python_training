from model.group_contact import Group_contact
from fixture.precond_verifi import precond_verifi_contact


def test_modify_contact_firstname(app):
    precond_verifi_contact(app)
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Group_contact(firstname="New_Name"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
