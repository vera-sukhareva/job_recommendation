from typing import List

from src.servicies.UserService import userService


class MessageConsumer:
    def consume(self, user_id: int, recommendations: List[str]):
        user = userService.get_by_id(user_id)
        user.recommendations = recommendations
        userService.update_user(user)
