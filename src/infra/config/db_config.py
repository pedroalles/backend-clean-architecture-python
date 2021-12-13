from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnectionHandler:
    """Sqlalchemy database connection"""

    def __init__(self) -> None:
        self.__conection_string = "sqlite:///storage.db"
        self.session = None

    def get_engine(self):
        """Returns connection Engine
        :param - None
        :return - engine connection to Database
        """
        engine = create_engine(self.__conection_string)
        return engine

    def __enter__(self):
        session_maker = sessionmaker()
        self.session = session_maker(bind=self.get_engine())
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
