from typing import List
from src.infra.config import DBConnectionHandler
from src.domain.models import Pets as PetsModels
from src.infra.entities import Pets

from src.data.interfaces import PetRepositoryInterface


class PetRepository(PetRepositoryInterface):
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

    @classmethod
    def select_pet(cls, pet_id: int = None, user_id: int = None) -> List[Pets]:
        """Select data in pets entity by pet_id and/or user_id
        :param - pet_id: Id of the registry
               - user_id: Id of the owner
        :return - List with Pets selected
        """

        try:
            query_data = None

            if pet_id and not user_id:
                with DBConnectionHandler() as db_connection:

                    data = db_connection.session.query(Pets).filter_by(id=pet_id).one()
                    query_data = [data]

            elif not pet_id and user_id:
                with DBConnectionHandler() as db_connection:

                    data = (
                        db_connection.session.query(Pets)
                        .filter_by(user_id=user_id)
                        .all()
                    )
                    query_data = data

            elif pet_id and user_id:
                with DBConnectionHandler() as db_connection:

                    data = (
                        db_connection.session.query(Pets)
                        .filter_by(id=pet_id, user_id=user_id)
                        .one()
                    )
                    query_data = [data]

            return query_data

        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()
