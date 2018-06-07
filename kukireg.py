# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import *
from fixture import app
import unittest, time, re
from model.user_data import User
from pdb import set_trace as bp

RandomUser = User.Random()


def test_register(app):
    app.go_to_main_page()
    app.registration(RandomUser)
    app.logout()
    app.go_to_login_page()
    app.login(RandomUser)
    assert app.is_logged_in()
    app.logout()

def test_login(app):
    app.go_to_login_page()
    assert app.is_not_logged_in()
    app.login(User.Admin())
    assert app.is_logged_in()
    app.logout()

def test_add_film(app):
    app.go_to_login_page()
    assert app.is_not_logged_in()
    app.login(User.Admin())
    assert app.is_logged_in()
    app.add_film_to_cart()
    assert app.is_not_empty()
    app.logout()

def test_del_film(app):
    app.go_to_login_page()
    # bp()
    app.login(User.Admin())
    app.del_film_from_cart()
    assert app.is_empty()
    app.logout()

def test_delete_profile(app):
    app.go_to_login_page()
    app.login(RandomUser)
    app.go_to_edit_page()
    app.delete_user_profile()
    assert app.is_not_logged_in()
