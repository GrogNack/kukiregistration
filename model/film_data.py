import random


class Film(object):

    def __init__(self, film_name="", film_number="", price=""):
        self.film_name = film_name
        self.film_number = film_number
        self.price = price

    @classmethod
    def Random(cls):
        return cls(film_number=random.randint(1,12))