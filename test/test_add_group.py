from model.group import Group

def test_add_group(app):
    app.session.login(user="admin", password="secret")
    app.group.open_groups_page()
    app.group.create(Group(name="New test group",
                           header="Test group header",
                           footer="Test group footer"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.login(user="admin", password="secret")
    app.group.open_groups_page()
    app.group.create(Group(name="",
                           header="",
                           footer=""))
    app.session.logout()

