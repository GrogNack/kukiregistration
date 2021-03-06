from selenium import webdriver
from model.application import Application
import pytest


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox", help="browser type")
    parser.addoption("--base_url", action="store", default="http://kuki.webtest2.htc-cs.com/", help="base URL")


@pytest.fixture(scope="module")
def browser_type(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="module")
def base_URL(request):
    return request.config.getoption("--base_url")

#Fixture.py
@pytest.fixture (scope="module")
def app(request, browser_type, base_URL):
    if browser_type == "firefox" :
        driver = webdriver.Firefox()
    elif browser_type == "chrome" :
        driver = webdriver.Chrome()
    elif browser_type == "ie" :
        driver = webdriver.ie
    request.addfinalizer(driver.quit)
    return Application(driver, base_URL)