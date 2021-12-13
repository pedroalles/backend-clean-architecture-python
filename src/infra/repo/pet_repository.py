from src.infra.config import DBConnectionHandler
from src.domain.models import Pets as PetsModels
from src.infra.entities import Pets


class PetRepository:
    """Class to manage Pet Repository"""

    @classmethod
    def insert_pet(cls, name: str, specie: str, age: int, user_id: id) -> Pets:
        """insert data in PetsEntity
        :param - name: name of the pet
               - specie: Enum with species acepted
               - age: pet age
               - user_id: id of the owner (fk)
        :return - tuple with new pet inserted
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_pet = Pets(name=name, specie=specie, age=age, user_id=user_id)
                db_connection.session.add(new_pet)
                db_connection.session.commit()

                return PetsModels(
                    id=new_pet.id,
                    name=new_pet.name,
                    specie=new_pet.specie.value,
                    age=new_pet.age,
                    user_id=new_pet.user_id,
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

            return None
