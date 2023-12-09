#!/usr/bin/python3
"""
defines the basemodel module
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """ The BaseModel class defines common attributes and methods that can be
    inherited by other classes in the application.

    Attributes:
        id (str): A universally unique identifier (UUID) for the object.
        created_at (datetime): indicating the object's creation time.
        updated_at (datetime): indicating the object's last update time.

    Methods:
        __init__: Initializes a new instance of the BaseModel class.
        __str__: Returns a string representation of the object.
        save: Updates the 'updated_at' attribute to the current timestamp.
        to_dict: Converts the object to a dictionary format.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.

        Args:
            *args: Variable-length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        date_format = "%Y-%m-%dT%H:%M:%S.%f"
                        self.__dict__[key] = datetime.strptime(
                                value, date_format)
                    else:
                        self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the object.

        Returns:
            str: A string containing the class name, id
        """
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the 'updated_at' attribute to the current timestamp.
        """

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Converts the object to a dictionary format.

        Returns:
            dict: A dictionary representation of the object.
        """
        obj = self.__dict__.copy()
        obj['__class__'] = self.__class__.__name__
        obj['created_at'] = self.created_at.isoformat()
        obj['updated_at'] = self.updated_at.isoformat()
        return obj
