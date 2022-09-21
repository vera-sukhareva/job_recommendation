from flask_restful import Resource
from flask import request

from src.servicies.UserService import userService


class UserController(Resource):
    def get(self):
        email = request.args['email']
        result = userService.get_result(email)
        return result
