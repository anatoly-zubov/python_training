from fixture.precond_verifi import precond_verifi_contact

def test_delete_first_contact(app):
    precond_verifi_contact(app)
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
