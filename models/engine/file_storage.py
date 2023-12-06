import json
from models.base_model import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        what_to_save = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(what_to_save, f)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                data = json.load(f)

                for key, obj in data.items():
                    self.__objects[key] = eval(obj["__class__"])(**obj)
        except FileNotFoundError:
            pass
