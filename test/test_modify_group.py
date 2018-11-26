from model.group import Group
from random import randrange

# пока что только первая группа

def test_modify_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name = "First group"))
    app.group.open_groups_page()
    old_groups = app.group.get_group_list()
    group = (Group(name="New test group edited", header="Test group header edited", footer="Test group footer edited"))
    group.id = old_groups[0].id
    app.group.edit_first(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

def test_modify_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name= "First group"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = (Group(name="bla bla", header="Test group header edited", footer="Test group footer edited"))
    group.id = old_groups[index].id
    app.group.edit_some_group(group, index)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_modify_first_group_name(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name= "First group"))
#     app.group.open_groups_page()
#
#     old_groups = app.group.get_group_list()
#     app.group.edit_first(Group(name="Modified name"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
#
#
# def test_modify_first_group_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name= "First group"))
#     app.group.open_groups_page()
#     old_groups = app.group.get_group_list()
#     app.group.edit_first(Group(header="Modified header"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
#
# def test_modify_first_group_footer(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name= "First group"))
#     app.group.open_groups_page()
#     old_group = app.group.get_group_list()
#     app.group.edit_first(Group(footer="Modified footer"))
#     new_groups = app.group.get_group_list()
#     assert len(old_group) == len(new_groups)
