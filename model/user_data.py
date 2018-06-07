import random


class User(object):

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    @classmethod
    def Admin(cls):
        return cls(username="test_user01@mail.ru", password="qwerty12")

    @classmethod
    def Random(cls):
        return cls(username="test_user" + str(random.randint(1, 99)) + "@mail.ru", password="qwerty12")