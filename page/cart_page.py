from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from page.internal_page import InternalPage


class CartPage(InternalPage):

    @property
    def remove_button(self):
        return self.driver.find_element(By.XPATH, "//*[@id='mycart']//i")

    @property
    def num_of_film(self):
        return self.driver.find_element(By.XPATH, "//*[@id='mycart']//span[@class='cart-count']")

    @property
    def film_title(self):
        return self.driver.find_element(By.XPATH, "//*[@id='mycart']/div[2]/div[2]/p")

    @property
    def film_board(self):
        return self.driver.find_element(By.XPATH, "//*[@id='mycart']//div[@class='cart-movie large-12 column mb1']")

    @property
    def list_film(self):
        return self.driver.find_elements(By.XPATH, "//*[@id='mycart']/descendant::p[@class='scale ptm']")

