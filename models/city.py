#!/usr/bin/python3
"""Defines the City module."""
from models.base_model import BaseModel


class City(BaseModel):
    """This is a class for City.
    Attributes:
        state_id (str): state id.
        name (str): city name.
    """

    state_id = ""
    name = ""

