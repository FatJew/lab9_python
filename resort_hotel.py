from hotel import Hotel
from dataclasses import dataclass


@dataclass
class ResortHotel(Hotel):
    """Class for ResortHotel type of Hotel."""

    name: str
    total_rooms: int
    rating: int
    pool_for_adults: bool
    pool_for_children: bool
    restaurant_count: int
    resort_name: str

    def get_location(self) -> str:
        """Returns the name of the Resort."""
        return self.resort_name
