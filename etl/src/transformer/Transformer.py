import pandas as pd


class Transformer:
    def transform(self, vacancies_df: pd.DataFrame) -> pd.DataFrame:
        cleaned_vacancies = vacancies_df[['Title', 'JobDescription', 'Location']].dropna()
        cleaned_vacancies['Title'] = cleaned_vacancies['Title'].str.strip().str.lower()
        cleaned_vacancies['JobDescription'] = cleaned_vacancies['JobDescription'].str.strip().str.lower()
        cleaned_vacancies['Location'] = cleaned_vacancies['Location'].str.strip().str.lower()
        return cleaned_vacancies


transformer = Transformer()
