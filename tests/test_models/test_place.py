import unittest
from models.base_model import BaseModel as BS
from models.place import Place

class TestPlace(unittest.TestCase):
    """A class to test the Place class."""

    def test_place_is_subclass_of_base_model(self):
        # check that Place inherits from BS
        self.assertTrue(issubclass(Place, BS))

    def test_place_has_attributes(self):
        # check that Place has the expected attributes
        place = Place()
        self.assertTrue(hasattr(place, "name"))
        self.assertTrue(hasattr(place, "city_id"))
        self.assertTrue(hasattr(place, "user_id"))
        self.assertTrue(hasattr(place, "description"))
        self.assertTrue(hasattr(place, "number_rooms"))
        self.assertTrue(hasattr(place, "number_bathrooms"))
        self.assertTrue(hasattr(place, "max_guest"))
        self.assertTrue(hasattr(place, "price_by_night"))
        self.assertTrue(hasattr(place, "latitude"))
        self.assertTrue(hasattr(place, "longitude"))
        self.assertTrue(hasattr(place, "amenity_ids"))

    def test_place_attributes_are_correct_types(self):
        # check that Place attributes have the correct types
        place = Place()
        place.name = "My place"
        place.city_id = "123"
        place.user_id = "456"
        place.description = "A nice place"
        place.number_rooms = 2
        place.number_bathrooms = 1
        place.max_guest = 4
        place.price_by_night = 100
        place.latitude = 37.5
        place.longitude = -122.4
        place.amenity_ids = ["789", "abc"]
        self.assertIsInstance(place.name, str)
        self.assertIsInstance(place.city_id, str)
        self.assertIsInstance(place.user_id, str)
        self.assertIsInstance(place.description, str)
        self.assertIsInstance(place.number_rooms, int)
        self.assertIsInstance(place.number_bathrooms, int)
        self.assertIsInstance(place.max_guest, int)
        self.assertIsInstance(place.price_by_night, int)
        self.assertIsInstance(place.latitude, float)
        self.assertIsInstance(place.longitude, float)
        self.assertIsInstance(place.amenity_ids, list)

if __name__ == '__main__':
    unittest.main()
