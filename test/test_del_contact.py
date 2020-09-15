from fixture.precond_verifi import precond_verifi_contact

def test_delete_first_contact(app):
    precond_verifi_contact(app)
    app.contact.delete_first_contact()
