import requests
import json
from src.constants import Config


class UserService():
    def sent_response(self, email):
        response = requests.get(Config.CORE_URL,
                                params={'email': email})
        return json.loads(response.content)


userService = UserService()
