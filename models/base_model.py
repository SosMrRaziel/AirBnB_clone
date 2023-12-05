#!/usr/bin/python3
import uuid
from datetime import datetime
"""define BaseModl class"""


class BaseModel:
    """BaseModel class that defines common
            attributes and methods for other classes"""
    def __init__(self):
        """Initialize a new BaseModel instance

        Attributes:
            id (str): a unique identifier for the instance
            created_at (datetime): the creation date and time of the instance
            updated_at (datetime): the last update date and time of th instance
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Return a string representation of the instance"""
        return "[{}] ({}) {}".format(
                    self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update the updated_at attribute with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary representation of the instance

        Returns:
            dict: a dictionary containing all the attributes and their values,
                with the class name under the key "__class__" and the datetime
                objects converted to ISO format strings
        """
        dic = self.__dict__.copy()
        dic["__class__"] = self.__class__.__name__
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        return dic
