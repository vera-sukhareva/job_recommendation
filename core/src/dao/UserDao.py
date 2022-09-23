from src.model.User import User
# from src.model.UserStatus import UserStatus


class UserDao:

    def find_by_email(self, email: str) -> User:
        user = User(email)
        user.id = "2"
        # user.status = UserStatus.PROCESSING
        # sql_find_user -> User
        return user

    def find_by_id(self, user_id: int) -> User:
        user = User("oij")
        # user.status = UserStatus.PROCESSING
        # sql_find_user -> User
        return user

    def save_user(self, user: User) -> User:
        # sql_save_user -> bool
        new_user = User(user.email)
        return new_user

    def update_user(self, user: User) -> User:
        # sql_save_user -> bool
        updated_user = User(user.email)
        return updated_user


userDao = UserDao()
