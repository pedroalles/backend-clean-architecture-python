from src.infra.config import DBConnectionHandler
from src.infra.entities import Users


class UserRepository:
    """Class to manage User Repository"""

    @classmethod
    def insert_user(cls, name: str, password: str):
        """insert data in user entity
        :param - name: user name
               - password: user password
        :return
        """

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
