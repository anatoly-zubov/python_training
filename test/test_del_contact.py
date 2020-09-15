from fixture.precond_verifi import precond_verification_contact

def test_delete_first_contact(app):
    precond_verification_contact(app)
    app.contact.delete_first_contact()
