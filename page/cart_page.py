from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from page.index_page import Page


class CartPage(Page):

    @property
    def remove_button(self):
        return self.driver.find_element(By.XPATH, "//*[@id='mycart']//i")
