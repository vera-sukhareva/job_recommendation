from typing import List

from src.db.Db import db
from src.db.Queries import Queries
from src.model.Vacancy import Vacancy


class VacancyDao:
    def find_all(self) -> List[Vacancy]:
        return db.session.execute(Queries.select_all_vacancies)

    def find_all_descriptions(self) -> List[str]:
        return db.session.execute(Queries.select_descriptions)


vacancyDao = VacancyDao()
