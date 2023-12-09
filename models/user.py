#!/usr/bin/python3
"""
Defines User module
"""
from models.base_model import BaseModel


class User(BaseModel):
    """create User class
    Attributes:
        email (str): user's email
        password (str): user's last_name
        first_name (str): user's first_name
        last_name (str): user's last_name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
