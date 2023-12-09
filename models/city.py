#!/usr/bin/python3
"""
Defines City module
"""
from models.base_model import BaseModel


class City(BaseModel):
    """create city class
    Attributes:
        state_id (str): state id
        name (str): state's name
    """
    state_id = ""
    name = ""
