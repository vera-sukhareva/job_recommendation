import requests
from src.constants import Config


class ResumeService():

    def sent_resume(self, resume_file):
        return requests.post(Config.CORE_URL,
                             files={'resume': resume_file})


resumeService = ResumeService()
