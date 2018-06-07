from page.index_page import Page
from selenium.webdriver.common.by import By
import random


class MainPage(Page):

    @property
    def filmpage_link(self):
        s = self.driver.find_elements(By.CSS_SELECTOR, "a.poster")
        count = random.randint(0,11)
        return s[count]

    @property
    def cart_link(self):
        return self.driver.find_element_by_css_selector("a[href='/cart']")

    @property
    def register_link(self):
        return self.driver.find_element_by_css_selector("a[href='/users/register']")

    @property
    def logout_link(self):
        return self.driver.find_element_by_css_selector("a[href='/users/logout']")