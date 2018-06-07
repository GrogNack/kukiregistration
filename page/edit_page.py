from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from page.index_page import Page


class EditPage (Page):

    @property
    def delete_button(self):
        return self.driver.find_element(By.XPATH, "//*[@class='button_to']//input[@type='submit']")