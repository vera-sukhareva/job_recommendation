import requests
import json
from src.constants import Urls


class UserService():
    def sent_response(self, email):
        response = requests.get(Urls.CORE_USERS_URL,
                                params={'email': email})
        return json.loads(response.content)


userService = UserService()
