import unittest
from models.base_model import BaseModel as BS
from models.city import City

class TestCity(unittest.TestCase):
    """A class to test the City class.

    This class inherits from the unittest.TestCase class and defines
    three test methods to check if the City class is a subclass of
    the BaseModel class, and if it has the name and state_id attributes
    with the correct types.
    """

    def test_city_is_subclass_of_base_model(self):
        # check that City inherits from BS
        self.assertTrue(issubclass(City, BS))

    def test_city_has_name_and_state_id_attributes(self):
        # check that City has name and state_id attributes
        city = City()
        self.assertTrue(hasattr(city, "name"))
        self.assertTrue(hasattr(city, "state_id"))

    def test_city_name_and_state_id_are_strings(self):
        # check that City name and state_id are strings
        city = City()
        city.name = "New York"
        city.state_id = "NY"
        self.assertIsInstance(city.name, str)
        self.assertIsInstance(city.state_id, str)

if __name__ == '__main__':
    unittest.main()
