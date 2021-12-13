from abc import ABC, abstractmethod
from typing import List
from src.domain.models import Users


class UserRepositoryInterface(ABC):
    """interface to User Repository"""

    @abstractmethod
    def insert_user(self, name: str, password: str) -> Users:
        """abstract method"""
        raise NotImplementedError

    @abstractmethod
    def select_user(self, user_id: int = None, name: str = None) -> List[Users]:
        """abstract method"""
        raise NotImplementedError
