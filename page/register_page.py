from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import random


class RegisterPage(object):

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @property
    def username_field(self):
        return self.driver.find_element_by_id("user_email")

    @property
    def password_field(self):
        return self.driver.find_element_by_id("user_password")

    @property
    def confirm_password_field(self):
        return self.driver.find_element_by_id("user_password_confirmation")

    @property
    def submit_button(self):
        return self.driver.find_element_by_name("commit")