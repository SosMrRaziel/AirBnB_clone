import json
from models.base_model import BaseModel as BM

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects
    
    def new(self, obj):
        self.__objects = setattr(self, obj.__class__.__name__.id, obj)
    
    def save(self):
        with open(self.__file_path, 'w') as f:
            json.dump(self.__objects, f)

    def reload(self):
        with open(self.__file_path, 'r') as f:
            if f:
                self.__objects = json.load(f)
            else:
                pass
    
