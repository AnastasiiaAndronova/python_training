from model.group import Group

# пока что только первая группа

def test_modify_first_group(app):
    app.group.open_groups_page()
    app.group.edit_first(Group(name="New test group edited", header="Test group header edited", footer="Test group footer edited"))

def test_modify_first_group_name(app):
    app.group.open_groups_page()
    app.group.edit_first(Group(name="Modified name"))

def test_modify_first_group_header(app):
    app.group.open_groups_page()
    app.group.edit_first(Group(header="Modified header"))

def test_modify_first_group_footer(app):
    app.group.open_groups_page()
    app.group.edit_first(Group(footer="Modified footer"))
