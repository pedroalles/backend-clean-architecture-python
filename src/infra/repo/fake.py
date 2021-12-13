from src.infra.config import DBConnectionHandler
from src.infra.entities import Users


class FakeRepo:
    """A simple Repository"""

    @classmethod
    def insert_use(cls, name: str, password: str):
        "something"

        with DBConnectionHandler() as db_connection:
            try:
                new_user = Users(name=name, password=password)
                db_connection.session.add(new_user)
                db_connection.session.commit()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
