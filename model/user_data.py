class User(object):

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    @classmethod
    def User(cls):
        return cls(username="test_user02@mail.ru", password="qwerty12")

    @classmethod
    def Admin(cls):
        return cls(username="test_user01@mail.ru", password="qwerty12")