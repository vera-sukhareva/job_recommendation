from src.Etl import etl

VACANCIES_DATA = 'data/data_job_posts.csv'

if __name__ == '__main__':
    etl.execute(VACANCIES_DATA)
