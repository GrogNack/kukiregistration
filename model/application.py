from selenium.common.exceptions import *
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from page.login_page import LoginPage
from page.main_page import MainPage
from page.cart_page import CartPage
from page.register_page import RegisterPage



class Application(object):

    def __init__(self, driver):
        self.driver = driver
        self.login_page = LoginPage(driver)
        self.main_page = MainPage(driver)
        self.cart_page = CartPage(driver)
        self.register_page = RegisterPage(driver)
        self.wait = WebDriverWait(driver, 10)

    def go_to_main_page(self):
        self.driver.get("http://kuki.webtest2.htc-cs.com/")

    def go_to_login_page(self):
        self.driver.get("http://kuki.webtest2.htc-cs.com/users/login")

    def go_to_film_page(self):
        self.driver.get("http://kuki.webtest2.htc-cs.com/movies/12")

    def login(self, user):
        lp = self.login_page
        lp.username_field.clear()
        lp.username_field.send_keys(user.username)
        lp.password_field.clear()
        lp.password_field.send_keys(user.password)
        lp.submit_button.click()

    def logout(self):
        mp = self.main_page
        mp.logout_link.click()

    def add_film_to_cart(self):
        fp = self.main_page
        cp = self.cart_page
        fp.filmpage_link.click()
        fp.add_to_button.click()
        fp.cart_link.click()
        cp.remove_button.click()

    def registration(self, user):
        mp = self.main_page
        rp = self.register_page
        mp.register_link.click()
        rp.username_field.clear()
        rp.username_field.send_keys(user.username)
        rp.password_field.clear()
        rp.password_field.send_keys(user.password)
        rp.confirm_password_field.clear()
        rp.confirm_password_field.send_keys(user.password)
        rp.submit_button.click()

    def is_logged_in(self):
        try:
            self.wait.until(presence_of_element_located((By.CSS_SELECTOR,"a[href='/cart']")))
            return True
        except WebDriverException:
            return False

    def is_not_logged_in(self):
        try:
            self.wait.until(presence_of_element_located((By.CSS_SELECTOR,"a[href='/users/login']")))
            return True
        except WebDriverException:
            return False

