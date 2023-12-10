#!/usr/bin/python3
import unittest
from models.engine.file_storage import FileStorage
import models
from models.base_model import BaseModel
from models.user import User
"""FileStorage test"""

class TestFilesStorage(unittest.TestCase):
    """a testing of all possible cases .. not all but most of them"""

    def test_instance(self):
        self.assertIs(FileStorage, type(FileStorage()))
        self.assertIsInstance(FileStorage.__objects, dict)
        self.assertIsInstance(FileStorage.__file_path, str)
    
    def test_NewStor(self):
        models.storage.new(BaseModel())
        models.storage.new(User())
        self.assertIn("BaseModel.{}".format(BaseModel().id),
                      models.storage.all().keys())
        self.assertIn("User.{}".format(User().id), models.storage.all().keys())

    def test_AllStorage(self):
        self.assertEqual(type(models.storage.all()), dict)
