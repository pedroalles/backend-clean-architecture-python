from faker import Faker
from src.infra.config import DBConnectionHandler
from .pet_repository import PetRepository

faker = Faker()
pet_repository = PetRepository()
db_connection_handler = DBConnectionHandler()


def delete_by_id(engine, id):
    query = f"DELETE FROM pets WHERE id='{id}';"
    engine.execute(query)


def test_insert_pet():
    """should inser pet in Pet table and return it"""

    name = faker.name()
    specie = "fish"
    age = faker.random_number(digits=1)
    user_id = faker.random_number()

    new_pet = pet_repository.insert_pet(
        name=name, specie=specie, age=age, user_id=user_id
    )

    engine = db_connection_handler.get_engine()
    query = f"SELECT * FROM pets WHERE id='{new_pet.id}';"
    query_pet = engine.execute(query).fetchone()

    assert new_pet.id == query_pet.id
    assert new_pet.name == query_pet.name
    assert new_pet.specie == query_pet.specie
    assert new_pet.age == query_pet.age
    assert new_pet.user_id == query_pet.user_id

    delete_by_id(engine, new_pet.id)


# def test_select_user():
#     """should select a user in Users table and compare it"""

#     user_id = faker.random_number(digits=5)
#     name = faker.name()
#     password = faker.word()
#     data = Users(id=user_id, name=name, password=password)
#     engine = db_connection_handler.get_engine()
#     query = f"INSERT INTO users (id, name, password) VALUES ('{user_id}', '{name}', '{password}')"
#     engine.execute(query)
#     query_user1 = user_repository.select_user(user_id=user_id)
#     query_user2 = user_repository.select_user(name=name)
#     query_user3 = user_repository.select_user(user_id=user_id, name=name)

#     assert data in query_user1
#     assert data in query_user2
#     assert data in query_user3

#     delete_by_id(engine, user_id)
