from src.model.Vacancy import Vacancy


class VacancyDao:
    def save(self, vacancy: Vacancy):
        print('saved', vacancy.title)


vacancyDao = VacancyDao()