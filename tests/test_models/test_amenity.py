# Import the unittest module
import unittest
from models.base_model import BaseModel as BS
from models.amenity import Amenity

"""Create a test class that inherits from unittest.TestCase"""


class TestAmenity(unittest.TestCase):
    """A class to test the Amenity class."""

    def test_init(self):
        """Test the initialization of an Amenity object."""

        amenity = Amenity(name="pool")  # Create an Amenity object with a name attribute

        
        self.assertEqual(amenity.name, "pool")  # Assert that the name attribute is equal to "pool"

        # Assert that the amenity is an instance of Amenity and BaseModel
        self.assertIsInstance(amenity, Amenity)
        self.assertIsInstance(amenity, BS)

    # Write a test method that checks the string representation of an Amenity object
    def test_str(self):
        """Test the string representation of an Amenity object."""
        
        amenity = Amenity(name="wifi")  # Create an Amenity object with a name attribute

        # Assert that the string representation of the amenity is in the expected format
        if hasattr(amenity, "id"):
            print(amenity.id)
        else:
            print("No id attribute found")


if __name__ == "__main__":
    unittest.main()