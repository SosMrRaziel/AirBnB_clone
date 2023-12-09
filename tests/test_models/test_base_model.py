#!/usr/bin/python3
"""
unittest for the basemodel module
"""

import unittest
from datetime import datetime
import time
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Testing BaseModel class"""

    def test_instances_type(self):
        obj = BaseModel()
        self.assertIs(BaseModel, type(obj))
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)
    
    def test_id_uniqueness(self):
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_created_at_two_timestamps(self):
        obj3 = BaseModel()
        time.sleep(0.03)
        obj4 = BaseModel()
        self.assertNotEqual(obj3.created_at, obj4.created_at)

    def test_str_format(self):
        obj = BaseModel()
        str_format = "[BaseModel] ({}) {}".format(obj.id, obj.__dict__)
        self.assertEqual(obj.__str__(), str_format)
    
    def test_save(self):
        obj = BaseModel()
        updated_before_save = obj.updated_at
        obj.save()
        updated_after_save = obj.updated_at
        self.assertNotEqual(updated_before_save, updated_after_save)

    def test_to_dict(self):
        obj = BaseModel()
        obj.name = "My First Model"
        obj.my_number = 78
        my_dict = obj.to_dict()
        self.assertIsInstance(my_dict, dict)
        self.assertIn("name", my_dict)
        self.assertIn("my_number", my_dict)
        self.assertIn("created_at", my_dict)
        self.assertIn("updated_at", my_dict)
        self.assertIn("__class__", my_dict)