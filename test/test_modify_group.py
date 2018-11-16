from model.group import Group

# пока что только первая группа

def test_modify_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name= "First group"))
    app.group.open_groups_page()
    app.group.edit_first(Group(name="New test group edited", header="Test group header edited", footer="Test group footer edited"))

def test_modify_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name= "First group"))
    app.group.open_groups_page()
    app.group.edit_first(Group(name="Modified name"))

def test_modify_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name= "First group"))
    app.group.open_groups_page()
    app.group.edit_first(Group(header="Modified header"))

def test_modify_first_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name= "First group"))
    app.group.open_groups_page()
    app.group.edit_first(Group(footer="Modified footer"))
