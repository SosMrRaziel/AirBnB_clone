#!/usr/bin/python3
from models.base_model import BaseModel as BS

class Review(BS):
    """class that inherit from BaseModel"""

    place_id = ""
    user_id = ""
    text = ""