from src.core import db
from src.model.user.UserStatus import UserStatus
from sqlalchemy import ARRAY


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    status = db.Column(db.Enum(UserStatus), default=UserStatus.FINISHED)
    resume_id = db.Column(db.Integer, db.ForeignKey('resume.id'))
    recommendations = db.Column(ARRAY(db.String))

    def __init__(self, email: str):
        self.email = email
