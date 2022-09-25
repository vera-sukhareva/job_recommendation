class Queries:
    table_vacancies = """
    CREATE TABLE IF NOT EXISTS vacancy(
    location VARCHAR,
    title   VARCHAR,
    creation_date TIMESTAMP,
    job_description VARCHAR,
    PRIMARY KEY ((location, title), creation_date )
);
"""
    KEYSPACE = "vacancy_keyspace"
    vacancy_keyspace = "CREATE KEYSPACE IF NOT EXISTS %s WITH REPLICATION = {'class': 'SimpleStrategy', 'replication_factor': 1};" % (
        KEYSPACE)

    truncate_vacancies = "TRUNCATE vacancy;"
    insert_vacancy = "INSERT INTO vacancy_keyspace.vacancy (location, title, creation_date, job_description) VALUES (%s, %s, %s, %s)"
