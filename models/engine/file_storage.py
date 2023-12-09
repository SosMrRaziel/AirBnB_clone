import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.review import Review
from models.state import State
from models.amenity import Amenity
from models.city import City


class FileStorage:
    """
    This class is responsible for storing
    and retrieving objects to and from a JSON file.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path).
        """
        what_to_save = {key: obj.to_dict() for key, obj
                        in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(what_to_save, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects
            (only if the JSON file (__file_path) exists).
        """
        try:
            with open(self.__file_path, 'r') as f:
                data = json.load(f)

                for key, obj in data.items():
                    self.__objects[key] = eval(obj["__class__"])(**obj)
        except FileNotFoundError:
            pass
