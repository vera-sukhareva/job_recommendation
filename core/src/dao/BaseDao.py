from src.core import db


class BaseDao:
    def commit(self):
        db.session.commit()
