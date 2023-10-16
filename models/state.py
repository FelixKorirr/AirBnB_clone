#!/usr/bin/python3
"""Define the State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """Represent state class.

    Attributes:
        name : The name of the state.
    """

    name = ""
