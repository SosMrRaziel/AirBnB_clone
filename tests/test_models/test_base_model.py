import unittest
from models.base_model import BaseModel as BS
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """Test class for BS"""

    def test_init(self):
        """Test the __init__ method of BS"""
        # Create a new instance of BS
        bm = BS()
        # Check if the id attribute is a string
        self.assertIsInstance(bm.id, str)
        # Check if the created_at and updated_at attributes are datetime objects
        self.assertIsInstance(bm.created_at, datetime)
        self.assertIsInstance(bm.updated_at, datetime)

    def test_str(self):
        """Test the __str__ method of BS"""
        # Create a new instance of BS
        bm = BS()
        # Check if the string representation is formatted correctly
        expected = "[{}] ({}) {}".format(
                    bm.__class__.__name__, bm.id, bm.__dict__)
        self.assertEqual(str(bm), expected)

    def test_save(self):
        """Test the save method of BS"""
        # Create a new instance of BS
        bm = BS()
        # Save the current updated_at attribute
        old_updated_at = bm.updated_at
        # Call the save method
        bm.save()
        # Check if the updated_at attribute has changed
        self.assertNotEqual(bm.updated_at, old_updated_at)

    def test_to_dict(self):
        """Test the to_dict method of BS"""
        # Create a new instance of BS
        bm = BS()
        # Call the to_dict method
        dic = bm.to_dict()
        # Check if the dictionary contains the correct keys and values
        self.assertIsInstance(dic, dict)
        self.assertEqual(dic["__class__"], bm.__class__.__name__)
        self.assertEqual(dic["id"], bm.id)
        self.assertEqual(dic["created_at"], bm.created_at.isoformat())
        self.assertEqual(dic["updated_at"], bm.updated_at.isoformat())

if __name__ == "__main__":
    unittest.main()