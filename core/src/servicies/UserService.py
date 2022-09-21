from typing import Dict

from src.dao.UserDao import userDao
from src.model.User import User
from src.model.UserStatus import UserStatus


class UserService:
    def get_result(self, email: str) -> Dict[str, str]:
        user = userDao.find_by_email(email)
        result = ''
        if not user:
            result = 'User not Found'
        elif user.status == UserStatus.PROCESSING:
            result = 'Please wait, resume is processing'
        elif user.status == UserStatus.FINISHED:
            result = user.recommendations
        return {'message': result}

    def get_by_email(self, email: str) -> User:
        return userDao.find_by_email(email)

    def get_by_id(self, user_id: int) -> User:
        return userDao.find_by_id(user_id)

    def update_user(self, user: User) -> User:
        return userDao.update_user(user)


userService = UserService()
