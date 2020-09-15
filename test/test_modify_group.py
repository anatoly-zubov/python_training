from model.group import Group
from fixture.precond_verifi import precond_verifi_group


def test_modify_group_name(app):
    precond_verifi_group(app)
    app.group.modify_first_group(Group(name="New_Group"))


def test_modify_group_header(app):
    precond_verifi_group(app)
    app.group.modify_first_group(Group(header="New_Header"))
