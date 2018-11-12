from model.group import Group

def test_modify_first_group(app):
    app.session.login(user="admin", password="secret")
    app.group.open_groups_page()
    app.group.edit_first(Group(name="New test group edited", header="Test group header edited", footer="Test group footer edited"))
    app.session.logout()

# пока что только первая группа