#!/usr/bin/python3
"""
define the user's module
"""
from models.base_model import BaseModel


class User(BaseModel):
    """class named User
    attributes:
    email(str):users email
    password(str): users password
    first name(str): users first name
    last name(str): users last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""