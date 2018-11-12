from model.group import Group

def test_delete_first_group(app):
    app.open_login_page()
    app.session.login(user="admin", password="secret")
    app.group.open_groups_page()
    app.group.delete_first_group()
    app.session.logout()