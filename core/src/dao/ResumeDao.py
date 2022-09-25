from src.core import db
from src.dao.BaseDao import BaseDao
from src.model.resume.Resume import Resume


class ResumeDao(BaseDao):
    def save_resume(self, resume: Resume):
        db.session.add(resume)
        self.commit()


resumeDao = ResumeDao()
