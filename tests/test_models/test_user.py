#!/usr/bin/python3
import unittest
from models.base_model import BaseModel as BS
from models.user import User

class TestUser(unittest.TestCase):
    """Test class for User"""

    def test_user_inherits_base_model(self):
        """Test that User inherits from BaseModel"""
        user = User() # create an instance of User
        # use assertIsInstance to check if user is an instance of BaseModel
        self.assertIsInstance(user, BS)

    def test_user_attributes(self): # define a test method for checking attributes
        """Test that User has the correct attributes"""
        user = User() # create an instance of User
        # use assertEqual to check if user has the expected attributes with empty values
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_user_save(self):
        """Test that User can save its attributes"""
        user = User() # create an instance of User
        # assign some values to the user attributes
        user.email = "test@test.com"
        user.password = "1234"
        user.first_name = "Test"
        user.last_name = "User"
        user.save() # call the save method
        # use assertEqual to check if user attributes are saved correctly
        self.assertEqual(user.email, "test@test.com")
        self.assertEqual(user.password, "1234")
        self.assertEqual(user.first_name, "Test")
        self.assertEqual(user.last_name, "User")

if __name__ == '__main__':
    unittest.main()
