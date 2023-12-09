#!/usr/bin/python3
"""
Defines Review module
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """create review class
    Attributes:
        place_id (str): place's id
        user_id (str): user's id
        text (str): text review
    """
    place_id = ""
    user_id = ""
    text = ""
