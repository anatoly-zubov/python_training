from model.group_contact import Group_contact


def test_modify_contact_firstname(app):
    app.contact.modify_first_contact(Group_contact(firstname="New_Name"))
