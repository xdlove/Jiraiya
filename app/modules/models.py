from flask_login import UserMixin


# user models
class User(UserMixin):
    def __init__(self):
        pass

    def is_authenticated(self):
        return True

    def is_actice(self):
        return True

    def is_anonymous(self):
        return True

    def get_id(self):
        return '1'

    @staticmethod
    def get_user(id):
        return User()

    @staticmethod
    def object():
        return None
