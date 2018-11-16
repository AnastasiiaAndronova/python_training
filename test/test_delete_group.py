from model.group import Group


def test_delete_first_group(app):
    app.group.open_groups_page()
    if app.group.count() == 0:
        app.group.create(Group())
    app.group.delete_first()

# пока что только первая группа