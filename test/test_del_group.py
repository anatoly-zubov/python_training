
from fixture.precond_verifi import precond_verifi_group


def test_delete_first_group(app):
    precond_verifi_group(app)
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)


