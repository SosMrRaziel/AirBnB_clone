#!/usr/bin/python3
from models.base_model import BaseModel as BS
"""class that inherit from BaseModel"""

class User(BS):
    """use class User that inherits from BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
