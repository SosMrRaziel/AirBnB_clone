#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()


    def __str__(self):
        return "{} {} {}".format(self.__class__.__name__ ,id = self.id, self.__dict__)
    
    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dic = self.__dict__.copy()
        dic["__class__"] = self.__class__.__name__
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        return dic

































