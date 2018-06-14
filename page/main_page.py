from page.index_page import Page
from selenium.webdriver.common.by import By
import random


class MainPage(Page):

# Internal page
    @property
    def filmpage_link(self):
        return self.driver.find_elements_by_css_selector("a.poster")


    @property
    def logout_link(self):
        return self.driver.find_element_by_css_selector("a[href='/users/logout']")

    @property
    def cart_link(self):
        return self.driver.find_element_by_css_selector("a[href='/cart']")

    @property
    def edit_link(self):
        return self.driver.find_element_by_css_selector("a[href='/users/edit']")

# External page
    @property
    def login_link(self):
        return self.driver.find_element_by_css_selector("a[href='/users/login']")

    @property
    def register_link(self):
        return self.driver.find_element_by_css_selector("a[href='/users/register']")




