from hotel import Hotel
from resort_hotel import ResortHotel
from motel import Motel
from typing import List, Optional


class HotelManager:
    """Class for managing multiple Hotel objects."""

    def __init__(self, hotels: List[Hotel]):
        self.hotels = hotels

    def __len__(self):
        """Returns the number of hotels in the manager."""
        return len(self.hotels)

    def __getitem__(self, index):
        """Returns the hotel at the specified index."""
        return self.hotels[index]

    def __iter__(self):
        """Returns an iterator over the hotels."""
        return iter(self.hotels)

    def display_hotels(self, hotels_list: Optional[List[Hotel]] = None) -> None:
        """Displays the hotels in the provided list. If no list is provided, displays all the hotels."""
        if hotels_list is None:
            hotels_list = self.hotels
        for hotel in hotels_list:
            print(hotel)

    def add_hotel(self, hotel: Hotel) -> None:
        """Adds a new Hotel to the list of hotels."""
        self.hotels.append(hotel)

    def find_all_with_room_greater_than(self, room: int = 100) -> List[Hotel]:
        """Finds and returns all the hotels with total rooms greater than the provided number."""
        return [hotel for hotel in self.hotels if hotel.total_rooms >= room]

    def find_with_pools(self) -> List[Hotel]:
        """Finds and returns all the ResortHotels with a pool for adults."""
        return [hotel for hotel in self.hotels if isinstance(hotel, ResortHotel) and hotel.pool_for_adults]

    def do_something_results(self) -> List:
        """Returns a list of results from calling the 'do_something()' method on each hotel."""
        return [hotel.get_location() for hotel in self.hotels]

    def concatenate_with_index(self) -> List[str]:
        """Returns a concatenation of each hotel's name with its index in the manager."""
        return enumerate(self.hotels)

    def zip_with_do_something_results(self) -> List[tuple]:
        """Returns a zip of each hotel's name and the result of calling 'do_something()' method on each hotel."""
        return list(zip(self.hotels,
                        self.do_something_results()))

    def attribute_values_by_type(self, data_type) -> dict:
        """Returns a dictionary with attribute names and values of a specific data type for each hotel."""
        return {attr: value for hotel in self.hotels for attr, value in hotel.__dict__.items()
                if isinstance(value, data_type)}

    def check_condition_all_any(self, condition) -> dict:
        """Checks if all or any hotels satisfy the provided condition and returns a dictionary of the results."""
        return {"all": all(condition(hotel) for hotel in self.hotels),
                "any": any(condition(hotel) for hotel in self.hotels)}


if __name__ == '__main__':
    hotel1 = ResortHotel("Resort1", 100, 4, True, True, 5, "Paradise Resort")
    hotel2 = Motel("Motel1", 50, 3, 1, 150, "CityA", "CityB")
    hotel3 = ResortHotel("Resort2", 200, 5, True, False, 8, "Beach Resort")

    hotel_manager = HotelManager([hotel1, hotel2, hotel3])
    hotel_manager.display_hotels()

    new_resort = ResortHotel("New Resort", 150, 4, False, True, 6, "Tropical Oasis")
    hotel_manager.add_hotel(new_resort)

    hotels_with_room_greater_than_100 = hotel_manager.find_all_with_room_greater_than(100)
    print("Hotels with room greater than 100:")
    hotel_manager.display_hotels(hotels_with_room_greater_than_100)

    hotels_with_pools = hotel_manager.find_with_pools()
    print("Hotels with pools:")
    hotel_manager.display_hotels(hotels_with_pools)

    do_something_results = hotel_manager.do_something_results()
    print("Results of 'do_something()' method:")
    print(do_something_results)

    concatenated_hotels = hotel_manager.concatenate_with_index()
    print("Concatenated hotel names with index:")
    print(list(concatenated_hotels))

    zip_results = hotel_manager.zip_with_do_something_results()
    print("Zipped results of 'do_something()' method with hotel names:")
    print(zip_results)

    attribute_values_int = hotel_manager.attribute_values_by_type(int)
    print("Attribute values of type 'int':")
    print(attribute_values_int)

    condition = lambda hotel: hotel.rating >= 4
    all_any_results = hotel_manager.check_condition_all_any(condition)
    print("Results of condition 'rating >= 4':")
    print(all_any_results)