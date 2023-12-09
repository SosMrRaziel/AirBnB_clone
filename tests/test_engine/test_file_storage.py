import unittest
from unittest import mock
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    """Test class for FileStorage"""

    def test_all(self):
        """Test the all method of FileStorage"""
        # Create a new instance of FileStorage
        fs = FileStorage()
        # Check if the __objects attribute is a dictionary
        self.assertIsInstance(fs._FileStorage__objects, dict)
        # Check if the all method returns the same dictionary
        self.assertIs(fs.all(), fs._FileStorage__objects)

    def test_new(self):
        """Test the new method of FileStorage"""
        # Create a new instance of FileStorage
        fs = FileStorage()
        # Create a new instance of BaseModel
        bm = BaseModel()
        # Call the new method with the BaseModel instance
        fs.new(bm)
        # Check if the __objects attribute contains the BaseModel instance
        # with the key
        key = "{}.{}".format(bm.__class__.__name__, bm.id)
        self.assertIn(key, fs._FileStorage__objects)
        self.assertIs(fs._FileStorage__objects[key], bm)

    @mock.patch("file_storage.open")
    def test_save(self, mock_open):
        """Test the save method of FileStorage"""
        # Create a new instance of FileStorage
        fs = FileStorage()
        # Create a mock file object
        mock_file = mock_open.return_value
        # Call the save method
        fs.save()
        # Check if the open function was called with the correct arguments
        mock_open.assert_called_once_with(fs._FileStorage__file_path, "w")
        # Check if the write method of the mock file object was called
        mock_file.write.assert_called_once()
        # Check if the write method was called with the correct argument
        # The argument should be a JSON string representation of the __objects
        # attribute
        expected = fs.to_json(fs._FileStorage__objects)
        mock_file.write.assert_called_with(expected)

    @mock.patch("file_storage.open")
    def test_reload(self, mock_open):
        """Test the reload method of FileStorage"""
        # Create a new instance of FileStorage
        fs = FileStorage()
        # Create a mock file object with some predefined content
        # The content should be a JSON string representation of a dictionary
        # that contains some BaseModel instances
        content = '{"BaseModel.123": {"id": "123", "created_at": "2021-12-09T18:37:51.000000", "updated_at": "2021-12-09T18:37:51.000000"}}'
        mock_file = mock_open.return_value
        mock_file.read.return_value = content
        # Call the reload method
        fs.reload()
        # Check if the open function was called with the correct arguments
        mock_open.assert_called_once_with(fs._FileStorage__file_path, "r")
        # Check if the read method of the mock file object was called
        mock_file.read.assert_called_once()
        # Check if the __objects attribute was updated with the content of the
        #  file object
        # The __objects attribute should be a dictionary that contains
        # BaseModel instances with the correct attributes
        self.assertIn("BaseModel.123", fs._FileStorage__objects)
        bm = fs._FileStorage__objects["BaseModel.123"]
        self.assertIsInstance(bm, BaseModel)
        self.assertEqual(bm.id, "123")
        self.assertEqual(bm.created_at.isoformat(), "2021-12-09T18:37:51.000000")
        self.assertEqual(bm.updated_at.isoformat(), "2021-12-09T18:37:51.000000")

if __name__ == "__main__":
    unittest.main()