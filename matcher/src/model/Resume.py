from typing import List


class Resume:
    id = None
    name = ""
    email = ""
    skills = []
    experience = []

    def __init__(self, name: str, email: str, skills: List[str], experience: List[str]):
        self.name = name
        self.email = email
        self.skills = skills
        self.experience = experience
