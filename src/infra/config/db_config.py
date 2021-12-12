from sqlalchemy import create_engine


class DBConnectionHandler:
    """Sqlalchemy database connection"""

    def __init__(self) -> None:
        self.__conection_string = "sqlite://storage.db"
        self.session = None

    def get_engine(self):
        """Returns connection Engine
        :param - None
        :return - engine connection to Database
        """
        engine = create_engine(self.__conection_string)
        return engine
