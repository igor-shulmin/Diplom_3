import pytest
from selenium import webdriver
from helpers import User


@pytest.fixture(params=['chrome', 'firefox'],scope='class')
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    if request.param == 'firefox':
        driver = webdriver.Firefox()

    request.cls.driver = driver

    yield

    driver.quit()

@pytest.fixture
def user(request):
    user = User()
    user.register_new_user_and_return_login_password()

    request.cls.user = user

    yield

    user.delete_user()
