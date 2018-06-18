# -*- coding: utf-8 -*-
from model.user_data import User
from model.film_data import Film
from pdb import set_trace as bp


randomUser = User.Random()
randomFilm = Film.Random()
current = "0"


# def test_register(app):
#     app.go_to_main_page()
#     app.smart_logout_full()
#     app.registration(randomUser)
#     app.logout()
#     app.smart_logout(randomUser)
#     # app.logout()
#     # app.go_to_login_page()
#     # app.login(randomUser)
#     assert app.is_logged_is_as(randomUser)
#     # app.logout()
#
# def test_login(app):
#     app.go_to_main_page()
#     app.smart_logout(User.Admin())
#     # app.go_to_login_page()
#     # app.login(User.Admin())
#     assert app.is_logged_is_as(User.Admin())
#     # app.logout()

def test_AddDel_film(app):
    app.go_to_main_page()
    app.smart_logout(User.Admin())
    # app.smart_logout_full()
    # app.go_to_login_page()
    # app.login(User.Admin())
    app.go_to_film_page(randomFilm)
    current = app.remember()
    # print("Cur1 " + current)
    app.add_film_to_cart(randomFilm)
    assert app.check_count_of_film_in_top(current, "add")
    app.go_to_cart_page()
    assert app.check_count_of_film_in_cart(current, "add")
    current = app.remember()
    # print("Cur2 " + current)
    # print("Film name " + randomFilm.film_name)
    assert app.equal_title(randomFilm)
    app.del_film_from_cart(randomFilm)
    assert app.check_count_of_film_in_top(current, "del")
    assert app.check_count_of_film_in_cart(current, "del")
    assert app.is_empty()
    # app.logout()

# def test_delete_profile(app):
#     app.go_to_main_page()
#     app.smart_logout(randomUser)
#     # app.go_to_login_page()
#     # app.login(randomUser)
#     app.go_to_edit_page()
#     app.delete_user_profile()
#     assert app.is_not_logged_in()
