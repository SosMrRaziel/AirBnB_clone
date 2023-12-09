#!/usr/bin/python3
"""
defines FileStorage module
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place


class FileStorage:
    """creates a class for file storage

    Attributes:
        file_path (str): path to the JSON file
        objects (dict): dictionary store all objects by <class name>.id
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        json_objs = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w", encoding="utf-8") as jf:
            json.dump(json_objs, jf)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                obj_data = json.load(f)
                for key, obj in obj_data.items():
                    self.__objects[key] = eval(obj["__class__"])(**obj)
        except FileNotFoundError:
            pass
