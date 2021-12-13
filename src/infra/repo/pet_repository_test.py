from faker import Faker
from src.infra.config import DBConnectionHandler
from src.infra.entities import Pets
from src.infra.entities.pets import AnimalTypes
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


def test_select_pet():
    """should select a pet in Pets table and compare it"""

    pet_id = faker.random_number(digits=5)
    name = faker.name()
    specie = "fish"
    age = faker.random_number(digits=1)
    user_id = faker.random_number()

    specie_mock = AnimalTypes("fish")
    data = Pets(id=pet_id, name=name, specie=specie_mock, age=age, user_id=user_id)

    engine = db_connection_handler.get_engine()
    query = (
        "INSERT INTO pets (id, name, specie, age, user_id)"
        + f"VALUES ('{pet_id}', '{name}', '{specie}', '{age}', '{user_id}');"
    )
    engine.execute(query)
    query_pet1 = pet_repository.select_pet(pet_id=pet_id)
    query_pet2 = pet_repository.select_pet(user_id=user_id)
    query_pet3 = pet_repository.select_pet(pet_id=pet_id, user_id=user_id)

    assert data in query_pet1
    assert data in query_pet2
    assert data in query_pet3

    delete_by_id(engine, pet_id)
