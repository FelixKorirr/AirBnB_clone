#!/usr/bin/python3
"""Define the subclass User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Represent superclass User class.

    Attributes:
        email : The user's email.
        password : The User's password.
        first_name : The User's first name.
        last_name : The User's last name.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
