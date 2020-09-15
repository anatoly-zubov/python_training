from model.group_contact import Group_contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Group_contact(firstname="Name"))
    app.contact.delete_first_contact()
