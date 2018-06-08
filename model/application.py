# -*- coding: utf-8 -*-
from selenium.common.exceptions import *
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from page.login_page import LoginPage
from page.main_page import MainPage
from page.cart_page import CartPage
from page.register_page import RegisterPage
from page.edit_page import EditPage
from page.film_page import FilmPage
from pdb import set_trace as bp



class Application(object):

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.login_page = LoginPage(driver, base_url)
        self.main_page = MainPage(driver, base_url)
        self.cart_page = CartPage(driver, base_url)
        self.register_page = RegisterPage(driver, base_url)
        self.edit_page = EditPage(driver, base_url)
        self.film_page = FilmPage(driver, base_url)
        self.wait = WebDriverWait(driver, 10)

    def go_to_main_page(self):
        self.driver.get(self.base_url)

    def go_to_login_page(self):
        self.driver.get(self.base_url + "users/login")

    def go_to_film_page(self, film):
        self.driver.get(self.base_url + "movies/" + str(film.film_number))

    def go_to_edit_page(self):
        self.driver.get(self.base_url + "users/edit")

    def go_to_cart_page(self):
        self.driver.get(self.base_url + "cart")

    # def smart_logout(self):
    #     element = self.wait.until(presence_of_element_located((By.CSS_SELECTOR,"a[href='/users/edit']")))
    #     if element.value_of_css_property("href") == "/users/edit" :
    #         bp()
    #         self.logout()

    def login(self, user):
        lp = self.login_page
        lp.username_field.clear()
        lp.username_field.send_keys(user.username)
        lp.password_field.clear()
        lp.password_field.send_keys(user.password)
        lp.submit_button.click()

    def delete_user_profile(self):
        ep = self.edit_page
        ep.delete_button.click()
        alert = self.driver.switch_to_alert()
        alert.accept()

    def logout(self):
        mp = self.main_page
        mp.logout_link.click()

    def add_film_to_cart(self, film):
        fp = self.film_page
        film.film_name = fp.film_title.text[0:-7]
        fp.add_to_button.click()

    def del_film_from_cart(self):
        mp = self.main_page
        cp = self.cart_page
        mp.cart_link.click()
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

# Проверка увеличения счётчика в верхнем меню
    def check_count_of_film_in_top(self, flag):
        fp = self.film_page
        num_film = fp.count_of_film
        # print(num_film.text)
        if flag == "add" :
            if num_film.text == "1" :
                return True
        elif flag == "del" :
            if num_film.text == "0" :
                return True

# Проверка увеличения счётчика на странице корзхины
    def check_count_of_film_in_cart(self, flag):
        cp = self.cart_page
        num_film = cp.num_of_film
        # print(num_film.text)
        if flag == "add" :
            if num_film.text == "1" :
                return True
        elif flag == "del" :
            if num_film.text == "0" :
                return True

# Проверка названия фильма
    def equal_title(self,film):
        cp = self.cart_page
        movie_title = cp.film_title.text
        # print(movie_title)
        # print(film.film_name)
        if movie_title == film.film_name :
            return True

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

    def is_empty(self):
        try:
            self.wait.until(invisibility_of_element_located((By.XPATH,"//*[@id='mycart']//div[@class='cart-movie large-12 column mb1']")))
            return True
        except WebDriverException:
            return False
