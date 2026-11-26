"""Shared base for every model."""
from abc import ABC, abstractmethod

from app.database import get_db


class BaseModel(ABC):
    @staticmethod
    def db():
        return get_db()

    @classmethod
    @abstractmethod
    def from_row(cls, row):
        """Turn a database row (dict) into an object. Return None if row is None."""
