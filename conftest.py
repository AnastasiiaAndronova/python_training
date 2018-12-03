from fixture.application import Application
import pytest

fixture = None


@ pytest.fixture
def app(request):
    global fixture

    browser = request.config.getoption("--browser")
    address = request.config.getoption("--address")

    if fixture is None:
       fixture = Application(browser=browser,address=address)
    else:
       if not fixture.is_valid():
           fixture = Application(browser=browser, address=address)

    fixture.session.ensure_login("admin", "secret")
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
    parser.addoption("--address", action = "store", default = "http://localhost/addressbook/")




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

