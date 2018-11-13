from model.group import Group

# пока что только первая группа

def test_modify_first_group(app):
    app.session.login()
    app.group.open_groups_page()
    app.group.edit_first(Group(name="New test group edited", header="Test group header edited", footer="Test group footer edited"))
    app.session.logout()

def test_modify_first_group_name(app):
    app.session.login()
    app.group.open_groups_page()
    app.group.edit_first(Group(name="Modified name"))
    app.session.logout()

def test_modify_first_group_header(app):
    app.session.login()
    app.group.open_groups_page()
    app.group.edit_first(Group(header="Modified header"))
    app.session.logout()

def test_modify_first_group_footer(app):
    app.session.login()
    app.group.open_groups_page()
    app.group.edit_first(Group(footer="Modified footer"))
    app.session.logout()