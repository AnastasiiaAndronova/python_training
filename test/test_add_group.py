from model.group import Group
import pytest
def test_add_group(app, db,json_groups,check_ui):
    group = json_groups
    old_groups = db.get_group_list()
    app.group.create(group)
    new_groups =db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(db.get_group_list(), key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


def test_add_empty_group(app,db):

    with pytest.allure.step('Given a group list'):
        old_groups = db.get_group_list()
    group = Group(name="", header='', footer='')
    with pytest.allure.step('When I add the group %s to the list' % group):
        app.group.create(group)
    with pytest.allure.step('Then the new group list is equal to the old list with  the added group'):
        new_groups =  db.get_group_list()
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

