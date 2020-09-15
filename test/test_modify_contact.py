from model.group_contact import Group_contact
from fixture.precond_verifi import precond_verification_contact


def test_modify_contact_firstname(app):
    precond_verification_contact(app)
    app.contact.modify_first_contact(Group_contact(firstname="New_Name"))
