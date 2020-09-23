from model.group import Group
from fixture.precond_verifi import precond_verifi_group


def test_modify_group_name(app):
    precond_verifi_group(app)
    old_groups = app.group.get_group_list()
    group = Group(name="New_Group")
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0]= group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)




#def test_modify_group_header(app):
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(header="New_Header"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups)  == len(new_groups)


