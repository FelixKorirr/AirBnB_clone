#!/usr/bin/python3
"""Defines subclass Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent an amenity.

    Attributes:
        name : The amenity's name.
    """

    name = ""
