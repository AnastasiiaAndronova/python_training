
def test_delete_first_group(app):
    app.session.login(user="admin", password="secret")
    app.group.open_groups_page()
    app.group.delete_first()
    app.session.logout()

# пока что только первая группа