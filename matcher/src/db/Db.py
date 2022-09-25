from cassandra.cluster import Cluster

from src.db.Queries import Queries


class Db:
    session = None
    cluster = None

    def __init__(self):
        self.cluster = Cluster()
        self.session = self.cluster.connect(Queries.KEYSPACE)


db = Db()
