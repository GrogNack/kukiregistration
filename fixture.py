from selenium import webdriver
from model.application import Application
import conftest
import pytest

@pytest.fixture (scope="module")
def app(request, browser_type, base_URL):
    if browser_type == "firefox" :
        driver = webdriver.Firefox()
    elif browser_type == "chrome" :
        driver = webdriver.Chrome()
    elif browser_type == "ie" :
        driver = webdriver.ie
    # request.addfinalizer(driver.quit)
    return Application(driver, base_URL)
