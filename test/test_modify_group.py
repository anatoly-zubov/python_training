from model.group import Group
from fixture.precond_verifi import precond_verifi_group


def test_modify_group_name(app):
    precond_verifi_group(app)
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="New_Group"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)




def test_modify_group_header(app):
    precond_verifi_group(app)
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(header="New_Header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups)  == len(new_groups)


