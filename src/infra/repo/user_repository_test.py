from faker import Faker
from src.infra.config import DBConnectionHandler
from .user_respository import UserRepository
from src.infra.entities import Users

faker = Faker()
user_repository = UserRepository()
db_connection_handler = DBConnectionHandler()


def delete_by_id(engine, id):
    query = f"DELETE FROM users WHERE id='{id}';"
    engine.execute(query)


def test_insert_user():
    """should inser User"""

    name = faker.name()
    password = faker.word()
    engine = db_connection_handler.get_engine()

    new_user = user_repository.insert_user(name, password)

    query = f"SELECT * FROM users WHERE id='{new_user.id}';"
    query_user = engine.execute(query).fetchone()

    # query = f"DELETE FROM users WHERE id='{new_user.id}';"
    # engine.execute(query)

    delete_by_id(engine, new_user.id)

    assert new_user.id == query_user.id
    assert new_user.name == query_user.name
    assert new_user.password == query_user.password


def test_select_user():
    """should select a user in Users table and compare it"""

    user_id = faker.random_number(digits=5)
    name = faker.name()
    password = faker.word()

    data = Users(id=user_id, name=name, password=password)

    engine = db_connection_handler.get_engine()
    query = f"INSERT INTO users (id, name, password) VALUES ('{user_id}', '{name}', '{password}')"
    engine.execute(query)

    query_user1 = user_repository.select_user(user_id=user_id)
    query_user2 = user_repository.select_user(name=name)
    query_user3 = user_repository.select_user(user_id=user_id, name=name)

    assert data in query_user1
    assert data in query_user2
    assert data in query_user3

    delete_by_id(engine, user_id)
