from page.index_page import Page
from selenium.webdriver.common.by import By
from pdb import set_trace as bp
from selenium.webdriver.support.expected_conditions import *


class FilmPage(Page):

    @property
    def add_to_button(self):
        return self.driver.find_element_by_css_selector("a.button")


