from model.group import Group
from random import randrange
import random

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

def test_modify_some_group_old(app):
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

def test_modify_some_group_db(app,db,check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name= "First group"))
    old_groups = db.get_group_list()
    group_edit = random.choice(old_groups)
    group = (Group(name="bla bla", header="Test group header edited", footer="Test group footer edited"))
    group.id =group_edit.id
    app.group.edit_some_group_by_id(group, group.id)
    #проверим количество записей в базе
    assert len(old_groups) == len(db.get_group_list())

    #загружаем данные из базы после изменения
    group_after_edit=db.get_group_list()

    #ищем в базе ту группу которую поменяли
    for edit in group_after_edit:
        if edit.id == group.id:
            # это та самая группа
            #проверим что поменялись данные именно в той группе
            assert edit==group
            #проверим что через UI
            if check_ui:
                assert sorted(group_after_edit, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
            return
    #если мы не нашли группу с тем же id  то ассерт
    assert 1==2


    new_groups = app.group.get_group_list()
#    old_groups[index] = group
#    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



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