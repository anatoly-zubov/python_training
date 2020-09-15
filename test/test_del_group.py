from fixture.precond_verifi import precond_verification


def test_delete_first_group(app):
    precond_verification(app)
    app.group.delete_first_group()

