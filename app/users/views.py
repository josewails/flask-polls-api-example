from flask import Blueprint

from flasgger import SwaggerView

users = Blueprint('users', __name__, url_prefix='/users')


class UserRegistration(SwaggerView):
    def post(self):
        return


class UserLogin(SwaggerView):
    def post(self):
        pass


class UserLogout(SwaggerView):
    def get(self):
        pass


class UserDetail(SwaggerView):
    def get(self):
        pass
