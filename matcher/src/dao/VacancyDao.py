from typing import List

from src.model.Vacancy import Vacancy


class VacancyDao:
    def find_all(self) -> List[Vacancy]:
        return [Vacancy('vac1', 'tokyo', 'cool job'),
                Vacancy('vac2', 'sapporo', 'not cool job'),
                Vacancy('vac3', 'kyoto', 'not cool job too'),
                Vacancy('vac4', 'osaka', 'too cool job'),
                Vacancy('vac5', 'kawasaki', 'not cool job at all')]

    def find_all_descriptions(self) -> List[str]:
        return ['1 Econometric Modelling Experts',
                '2 Lionbridge Internet Assessor',
                '3 Internet Assessor']


vacancyDao = VacancyDao()