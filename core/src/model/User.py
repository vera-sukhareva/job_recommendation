from src.model.UserStatus import UserStatus


class User:
    id = None
    email = ''
    status = UserStatus.FINISHED
    resume_id = None
    recommendations = []

    def __init__(self, email: str):
        self.email = email

