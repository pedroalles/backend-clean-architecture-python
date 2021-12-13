from abc import ABC, abstractmethod
from typing import List
from src.domain.models import Pets


class PetRepositoryInterface(ABC):
    """interface to Pet Repository"""

    @abstractmethod
    def insert_pet(self, name: str, specie: str, age: int, user_id: id) -> Pets:
        """abstract method"""
        raise NotImplementedError

    @abstractmethod
    def select_pet(self, pet_id: int = None, user_id: int = None) -> List[Pets]:
        """abstract method"""
        raise NotImplementedError
