from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import random


class EditPage (object):
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @property
    def delete_button(self):
        return self.driver.find_element(By.XPATH, "//*[@class='button_to']//input[@type='submit']")