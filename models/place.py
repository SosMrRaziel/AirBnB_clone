#!/usr/bin/python3
"""
Defines Place module
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """create Place class
    Attributes:
        city_id (str): the City id
        user_id (str): the User id
        name (str): place's name
        description (str): description of the place
        number_rooms (int): the number of rooms
        number_bathrooms (int): the number of bathrooms
        max_guest (int): the maximum number of guests
        price_by_night (int): the price by night of the place
        latitude (float): the latitude of the place
        longitude (float): the longitude of the place
        amenity_ids (list): list of Amenity's id
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
