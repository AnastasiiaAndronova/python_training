from fixture.application import Application
import pytest
import os
import os.path
import json

fixture = None
target = None

@ pytest.fixture
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    if target is None:
        with open(request.config.getoption("--target")) as config_file:
            target = json.load(config_file)
    if fixture is None or not fixture.is_valid():
       fixture = Application(browser=browser, base_url=target["BaseUrl"])
    fixture.session.ensure_login(username=target["username"], password= target["password"])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
   def fin():
       fixture.session.ensure_logout()
       fixture.destroy()
   request.addfinalizer(fin)
   return fixture

def pytest_addoption(parser):
    parser.addoption("--browser", action = "store", default = "chrome")
    parser.addoption("--target", action = "store", default = "target.json")




# Флаг для прерывания тестов
# fixture = None
# status = 0

# @ pytest.fixture
# def app():
#
#     global status
#     if status is 1:
#         pytest.exit("decided to stop the test run")
#     status = 1
#     global fixture
#     if fixture is None:
#         fixture = Application()
#     else:
#         if not fixture.is_valid():
#             fixture = Application()
#     fixture.session.ensure_login("admin", "secretоо")
#     return fixture
#
#
# @pytest.fixture(scope="session", autouse=True)
# def stop(request):
#     global status
#     status = 0
#     def fin():
#         fixture.session.ensure_logout()
#         fixture.destroy()
#     request.addfinalizer(fin)
#     return fixture

