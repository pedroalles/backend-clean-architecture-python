from faker import Faker
from src.infra.config import DBConnectionHandler
from .user_respository import UserRepository

faker = Faker()
user_repository = UserRepository()
db_connection_handler = DBConnectionHandler()


def test_insert_user():
    """should inser User"""

    name = faker.name()
    password = faker.word()
    engine = db_connection_handler.get_engine()

    new_user = user_repository.insert_user(name, password)

    query = f"SELECT * FROM users WHERE id='{new_user.id}';"
    query_user = engine.execute(query).fetchone()

    query = f"DELETE FROM users WHERE id='{new_user.id}';"
    engine.execute(query)

    assert new_user.id == query_user.id
    assert new_user.name == query_user.name
    assert new_user.password == query_user.password
