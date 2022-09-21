import pandas as pd


class Extractor:
    def extract(self, csv_file: str) -> pd.DataFrame:
        vacancies = pd.read_csv(csv_file)
        return vacancies


extractor = Extractor()
