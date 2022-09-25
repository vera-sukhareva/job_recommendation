from src.db.Queries import Queries
from src.model.Vacancy import Vacancy
from src.db.Db import db


class VacancyDao:
    def save(self, vacancy: Vacancy):
        db.session.execute(Queries.insert_vacancy, [vacancy.location, vacancy.title,
                                                    vacancy.creation_date, vacancy.job_description])

    def delete(self):
        db.session.execute(Queries.truncate_vacancies)


vacancyDao = VacancyDao()
