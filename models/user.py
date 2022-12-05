#!/usr/bin/python3
"""Defines the User module."""
from models.base_model import BaseModel


class User(BaseModel):
    """This is a class for user.
    Attributes:
        email (str): user's email.
        password (str): user password.
        first_name (str): first name of user.
        last_name (str): last name of user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

