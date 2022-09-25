from cassandra.cluster import Cluster

from src.db.Queries import Queries


class Db:
    session = None
    cluster = None

    def __init__(self):
        self.cluster = Cluster()
        self.session = self.cluster.connect()
        self._create_keyspace()
        self.session.set_keyspace(Queries.KEYSPACE)
        self._create_tables()

    def _create_keyspace(self):
        self.session.execute(Queries.vacancy_keyspace)

    def _create_tables(self):
        self.session.execute(Queries.table_vacancies)


db = Db()
