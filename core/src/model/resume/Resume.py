from typing import List
from sqlalchemy import ARRAY

from src.core import db


class Resume(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    skills = db.Column(ARRAY(db.String))
    experience = db.Column(ARRAY(db.String))

    def __init__(self, name: str, email: str, skills: List[str], experience: List[str]):
        self.name = name
        self.email = email
        self.skills = skills
        self.experience = experience

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'skills': self.skills,
            'experience': self.experience
        }
