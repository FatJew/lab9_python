from hotel import Hotel
from dataclasses import dataclass


@dataclass
class Motel(Hotel):
    """Class for Motel type of Hotel."""

    name: str
    total_rooms: int
    rating: int
    highway_number: int
    distance_km: int
    city_from: str
    city_to: str

    def get_location(self) -> str:
        """Returns the location of the Motel."""
        return f"{self.city_from}-{self.city_to}, {self.distance_km}km"
