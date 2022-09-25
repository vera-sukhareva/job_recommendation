from pyresparser import ResumeParser
import os

from src.model.resume.Resume import Resume
from src.dao.ResumeDao import resumeDao


class ResumeService:

    def parse(self, resume_file) -> Resume:
        file_path = 'data/' + resume_file.filename
        resume_file.save(file_path)
        parsed = ResumeParser(file_path).get_extracted_data()
        os.remove(file_path)
        return self._map_to_resume(parsed)

    def save_resume(self, resume: Resume) -> Resume:
        resumeDao.save_resume(resume)
        return resume

    def _map_to_resume(self, parsed_data: dict) -> Resume:
        return Resume(
            parsed_data['name'],
            parsed_data['email'],
            parsed_data['skills'],
            parsed_data['experience']
        )


resumeService = ResumeService()
