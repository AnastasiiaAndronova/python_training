import pytest
from group import Group
from application import Application


@ pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.open_home_page()
    app.login(user="admin", password="secret")
    app.open_groups_page()
    app.open_add_group_page()
    app.create_group(Group(name="New test group", header="Test group header", footer="Test group footer"))
    app.return_to_groups_page()
    app.logout()

def test_add_empty_group(app):
    app.open_home_page()
    app.login(user="admin", password="secret")
    app.open_groups_page()
    app.open_add_group_page()
    app.create_group(Group(name="", header="", footer=""))
    app.return_to_groups_page()
    app.logout()

