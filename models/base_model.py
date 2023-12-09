#!/usr/bin/python3
"""define BaseModl class"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """BaseModel class that defines common
            attributes and methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance

        Attributes:
            id (str): a unique identifier for the instance
            created_at (datetime): the creation date and time of the instance
            updated_at (datetime): the last update date and time of th instance
        """

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        value = datetime.strptime(value,
                                                  '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Return a string representation of the instance"""

        return "[{}] ({}) {}".format(
                    self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update the updated_at attribute with the current datetime"""

        self.updated_at = datetime.now()
        models.storage.save()

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
