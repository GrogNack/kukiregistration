# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import *
from fixture import app
import unittest, time, re
from model.user_data import User


def test_register(app):
    app.go_to_main_page()
    app.registration(User.Admin())
