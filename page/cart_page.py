from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class CartPage(object):

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @property
    def remove_button(self):
        s = self.driver.find_elements(By.TAG_NAME, "i")
        return s[2]
