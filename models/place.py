#!/usr/bin/python3
"""Defines the Place module."""
from models.base_model import BaseModel


class Place(BaseModel):
    """This is a class for place.
    Attributes:
        city_id (str): city id.
        user_id (str): user id.
        name (str): place name.
        description (str): description of place.
        number_rooms (int): number of rooms in place.
        number_bathrooms (int): number of bathrooms in place.
        max_guest (int): maximum number of guests in place.
        price_by_night (int): price by night.
        latitude (float): latitude of place.
        longitude (float): longitude of place.
        amenity_ids (list): list of Amenity id.
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

