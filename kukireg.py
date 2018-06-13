# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import *
from fixture import app
import unittest, time, re
from model.user_data import User
from model.film_data import Film
from pdb import set_trace as bp
import random

randomUser = User.Random()
randomFilm = Film.Random()


def test_register(app):
    app.go_to_main_page()
    app.smart_logout_full()
    app.registration(randomUser)
    app.smart_logout(randomUser)
    # app.logout()
    # app.go_to_login_page()
    # app.login(randomUser)
    assert app.is_logged_is_as(randomUser)
    # app.logout()

def test_login(app):
    app.go_to_main_page()
    app.smart_logout(User.Admin())
    # app.go_to_login_page()
    # app.login(User.Admin())
    assert app.is_logged_is_as(User.Admin())
    # app.logout()

def test_AddDel_film(app):
    app.go_to_main_page()
    app.smart_logout(User.Admin())
    # app.go_to_login_page()
    # app.login(User.Admin())
    app.go_to_film_page(randomFilm)
    app.add_film_to_cart(randomFilm)
    assert app.check_count_of_film_in_top("add")
    app.go_to_cart_page()
    assert app.check_count_of_film_in_cart("add")
    assert app.equal_title(randomFilm)
    app.del_film_from_cart()
    assert app.check_count_of_film_in_top("del")
    assert app.check_count_of_film_in_cart("del")
    assert app.is_empty()
    # app.logout()

def test_delete_profile(app):
    app.go_to_main_page()
    app.smart_logout(randomUser)
    # app.go_to_login_page()
    # app.login(randomUser)
    app.go_to_edit_page()
    app.delete_user_profile()
    assert app.is_not_logged_in()
