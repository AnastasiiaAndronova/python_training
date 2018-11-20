from model.group import Group

def test_add_group(app):
    current_groups = app.group.get_group_list()
    app.group.create(Group(name="New test group",
                           header="Test group header",
                           footer="Test group footer"))
    new_groups = app.group.get_group_list()
    assert len(current_groups) + 1 == len(new_groups)


def test_add_empty_group(app):
    current_groups = app.group.get_group_list()
    app.group.create(Group())
    new_groups = app.group.get_group_list()
    assert len(current_groups) + 1 == len(new_groups)

