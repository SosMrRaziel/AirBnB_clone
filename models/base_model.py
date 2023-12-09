#!/usr/bin/python3
"""
Defines BaseModel module
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    creates BaseModel parent class
    """

    def __init__(self, *args, **kwargs):
        """
        __init__ the class constructor, initializes all instance attributes

        Args:
            *args: unused arguments
            **kwargs (dict): key/value pairs
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        f_date = "%Y-%m-%dT%H:%M:%S.%f"
                        self.__dict__[key] = datetime.strptime(value, f_date)
                    else:
                        self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """returns the BaseModel str representation"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id,
                                     self.__dict__)

    def save(self):
        """updates the public attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing:
            all keys/values of __dict__
            a key __class__ with the class name of the object
        for created_at and updated_at keys are converted
        to string object in ISO format
        """
        new = self.__dict__.copy()
        new["__class__"] = self.__class__.__name__
        new["created_at"] = self.created_at.isoformat()
        new["updated_at"] = self.updated_at.isoformat()
        return new
