#!/usr/bin/python3
"""
defines storage module
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
     serializes instances to a JSON file and deserialize
     file_path: path to the json file
     objects: dic that stores all objects
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        data_to_save = {key: obj.to_dict()
                        for key, obj in self.__objects.items()}

        with open(self.__file_path, 'w', encoding="utf-8") as jfile:
            json.dump(data_to_save, jfile)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as pfile:
                data_loaded = json.load(pfile)

                for key, obj_data in data_loaded.items():
                    self.__objects[key] = eval(obj_data["__class__"])(
                        **obj_data)
        except FileNotFoundError:
            pass
