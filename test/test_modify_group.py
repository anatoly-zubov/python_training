from random import randrange
from model.group import Group
from fixture.precond_verifi import precond_verifi_group


def test_modify_group_name(app):
    precond_verifi_group(app)
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="New_Group")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(group,index)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index]= group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)




#def test_modify_group_header(app):
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(header="New_Header"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups)  == len(new_groups)


