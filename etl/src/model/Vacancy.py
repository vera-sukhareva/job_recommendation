from datetime import datetime


class Vacancy:
    creation_date = datetime.now()
    title = ''
    location = ''
    job_description = ''

    def __init__(self, title: str, location: str, job_description: str):
        self.title = title
        self.location = location
        self.job_description = job_description