from src.core import db
from src.dao.BaseDao import BaseDao
from src.model.user.User import User


class UserDao(BaseDao):

    def find_by_email(self, email: str) -> User:
        user = User.query.filter_by(email=email).first()
        return user

    def find_by_id(self, user_id: int) -> User:
        user = User.query.get(user_id)
        return user

    def save_user(self, user: User):
        db.session.add(user)
        self.commit()

    def update_user(self):
        self.commit()


userDao = UserDao()
