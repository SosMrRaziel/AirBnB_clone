#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self, id, created_at, updated_at):
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at

        id = str(uuid.uuid4())
        
        updated_at = datetime.now()

    def __str__(self):
        return "[BaseModel] {} {}".format(id = self.id, self.__dict__)
    
    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dic = "BaseModel(id={self.id}, created_at={self.created_at}, updated_at={self.updated_at})".format(())




































#     def __repr__(self):
#         return f"BaseModel(id={self.id}, created_at={self.created_at}, updated_at={self.updated_at})"
    
# id = str(uuid.uuid4())
# created_at = datetime.now()
# updated_at = datetime.now()

# base_model = BaseModel(id, created_at, updated_at)
# print(base_model)

# base_model1 = BaseModel(id, created_at, updated_at)
# print(base_model1.__dict__)

