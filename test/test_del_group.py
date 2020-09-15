
from fixture.precond_verifi import precond_verifi_group


def test_delete_first_group(app):
    precond_verifi_group(app)
    app.group.delete_first_group()

