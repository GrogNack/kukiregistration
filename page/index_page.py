from selenium.webdriver.support.wait import WebDriverWait


class Page(object):

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, 10)