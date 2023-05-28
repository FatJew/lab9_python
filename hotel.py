from abc import ABC, abstractmethod


class Hotel(ABC):
    """Base class for different types of hotels."""

    @abstractmethod
    def get_location(self) -> str:
        """Abstract method for getting the location of the hotel."""
        pass
