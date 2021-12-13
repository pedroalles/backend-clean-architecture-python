from faker import Faker
from .user_respository import UserRepository

faker = Faker()

user_repository = UserRepository()


def test_insert_user():
    """should inser User"""

    name = faker.name()
    password = faker.word()

    new_user = user_repository.insert_user(name, password)
    print(new_user)
