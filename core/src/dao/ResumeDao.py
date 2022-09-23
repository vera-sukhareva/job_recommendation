from src.model.Resume import Resume


class ResumeDao:
    def save_resume(self, resume: Resume) -> Resume:
        # sql_save_resume
        new_resume = resume
        new_resume.id="0"
        return new_resume


resumeDao = ResumeDao()