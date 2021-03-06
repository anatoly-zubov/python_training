from random import randrange
from fixture.precond_verifi import precond_verifi_group


def test_delete_some_group(app):
    precond_verifi_group(app)
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[index:index+1] = []
    assert old_groups == new_groups


