import unittest
import tempfile
import json
from models.engine.file_storage import FileStorage

""" Define some sample classes and
objects to test the FileStorage class """


class FileStorageTest(unittest.TestCase):
    """
    A class that contains a unit test for the FileStorage class.

    Attributes:
        temp_file (file): A temporary file for testing the FileStorage class.
        file_storage (FileStorage): An instance of the FileStorage class.
    """

    # Set up a temporary file for each test
    def setUp(self):
        """
        Creates a temporary file and a FileStorage instance for each test.
        """
        self.temp_file = tempfile.NamedTemporaryFile()
        self.file_storage = FileStorage(self.temp_file.name)

    # Clean up the temporary file after each test
    def tearDown(self):
        """
        Closes and deletes the temporary file after each test.
        """
        self.temp_file.close()

    # Test the new method
    def test_new(self):
        """
        Tests the new method of the FileStorage class.

        Checks that the new method adds
        the given objects to the __objects dictionary
        with the correct keys and values.
        """
        # Add two objects to the file storage
        self.file_storage.new(user1)
        self.file_storage.new(user2)
        # Check that the objects are in the __objects dictionary
        self.assertIn("User.1", self.file_storage.all())
        self.assertIn("User.2", self.file_storage.all())
        self.assertEqual(self.file_storage.all()["User.1"], user1)
        self.assertEqual(self.file_storage.all()["User.2"], user2)

    # Test the save method
    def test_save(self):
        """
        Tests the save method of the FileStorage class.

        Checks that the save method serializes
        the __objects dictionary to the JSON file
        with the correct data format.
        """
        # Add two objects to the file storage
        self.file_storage.new(user1)
        self.file_storage.new(user2)
        # Save the objects to the JSON file
        self.file_storage.save()
        # Read the JSON file and compare with the expected data
        with open(self.temp_file.name, "r") as f:
            data = json.load(f)
            expected_data = {
                "User.1": {
                    "__class__": "User",
                    "id": 1,
                    "name": "Alice",
                    "email": "alice@example.com"
                },
                "User.2": {
                    "__class__": "User",
                    "id": 2,
                    "name": "Bob",
                    "email": "bob@example.com"
                }
            }
            self.assertEqual(data, expected_data)

    # Test the reload method
    def test_reload(self):
        """
        Tests the reload method of the FileStorage class.

        Checks that the reload method deserializes
        the JSON file to the __objects dictionary
        with the correct object instances.
        """
        # Write some data to the JSON file
        with open(self.temp_file.name, "w") as f:
            data = {
                "User.1": {
                    "__class__": "User",
                    "id": 1,
                    "name": "Alice",
                    "email": "alice@example.com"
                },
                "User.2": {
                    "__class__": "User",
                    "id": 2,
                    "name": "Bob",
                    "email": "bob@example.com"
                }
            }
            json.dump(data, f)
        # Reload the data from the JSON file
        self.file_storage.reload()
        # Check that the objects are in the __objects dictionary
        self.assertIn("User.1", self.file_storage.all())
        self.assertIn("User.2", self.file_storage.all())
        self.assertEqual(self.file_storage.all()["User.1"].id, 1)
        self.assertEqual(self.file_storage.all()["User.1"].name, "Alice")
        self.assertEqual(self.file_storage.all()["User.1"].email,
                         "alice@example.com")
        self.assertEqual(self.file_storage.all()["User.2"].id, 2)
        self.assertEqual(self.file_storage.all()["User.2"].name, "Bob")
        self.assertEqual(self.file_storage.all()["User.2"].email,
                         "bob@example.com")


if __name__ == "__main__":
    unittest.main()
