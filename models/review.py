#!/usr/bin/python3
"""Defines the Review module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """This a class for Review.
    Attributes:
        place_id (str): place id.
        user_id (str): user id.
        text (str): text for review.
    """

    place_id = ""
    user_id = ""
    text = ""

