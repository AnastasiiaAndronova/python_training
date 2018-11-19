from model.group import Group

def test_add_group(app):
    app.group.create(Group(name="New test group",
                           header="Test group header",
                           footer="Test group footer"))


def test_add_empty_group(app):
    app.group.create(Group())

