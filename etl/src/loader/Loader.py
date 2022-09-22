import pandas as pd

from src.dao.VacancyDao import vacancyDao
from src.model.Vacancy import Vacancy


class Loader:

    def load(self, vacancies: pd.DataFrame):
        for index, row in vacancies.iterrows():
            new_vacancy = Vacancy(title=row.Title,
                                  location=row.Location,
                                  job_description=row.JobDescription)
            vacancyDao.save(new_vacancy)


loader = Loader()