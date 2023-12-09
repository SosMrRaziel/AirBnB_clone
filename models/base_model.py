# #!/usr/bin/python3

# import uuid
# from datetime import datetime
# import models

# """define BaseModl class"""


# class BaseModel:
#     """BaseModel class that defines common
#             attributes and methods for other classes"""

#     def __init__(self, *args, **kwargs):
#         """Initialize a new BaseModel instance

#         Attributes:
#             id (str): a unique identifier for the instance
#             created_at (datetime): the creation date and time of the instance
#             updated_at (datetime): the last update date and time of th instance
#         """

#         if kwargs:
#             for key, value in kwargs.items():
#                 if key != '__class__':
#                     if key in ('created_at', 'updated_at'):
#                         value = datetime.strptime(value,
#                                                   '%Y-%m-%dT%H:%M:%S.%f')
#                     setattr(self, key, value)
#         else:
#             self.id = str(uuid.uuid4())
#             self.created_at = self.updated_at = datetime.now()
#             models.storage.new(self)

#     def __str__(self):
#         """Return a string representation of the instance"""

#         return "[{}] ({}) {}".format(
#                     self.__class__.__name__, self.id, self.__dict__)

#     def save(self):
#         """Update the updated_at attribute with the current datetime"""

#         self.updated_at = datetime.now()
#         models.storage.save()

#     def to_dict(self):
#         """Return a dictionary representation of the instance

#         Returns:
#             dict: a dictionary containing all the attributes and their values,
#                 with the class name under the key "__class__" and the datetime
#                 objects converted to ISO format strings
#         """

#         dic = self.__dict__.copy()
#         dic["__class__"] = self.__class__.__name__
#         dic["created_at"] = self.created_at.isoformat()
#         dic["updated_at"] = self.updated_at.isoformat()
#         return dic
#!/usr/bin/python3

import uuid
from datetime import datetime
import models

"""
defines all common attributes/methods for other classes
"""


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
