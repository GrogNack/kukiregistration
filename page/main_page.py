from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import random


class MainPage(object):

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @property
    def filmpage_link(self):
        s = self.driver.find_elements(By.CSS_SELECTOR, "a.poster")
        count = random.randint(0,11)
        return s[count]

    @property
    def cart_link(self):
        return self.driver.find_element_by_css_selector("a[href='/cart']")

    @property
    def add_to_button(self):
        return self.driver.find_element_by_css_selector("a.button")

    @property
    def register_link(self):
        return self.driver.find_element_by_css_selector("a[href='/users/register']")