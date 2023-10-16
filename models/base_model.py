#!/usr/bin/env python3
"""Define superclass called BaseModel."""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Represent superclass."""

    def __init__(self, *args, **kwargs):
        """
        Initialize the new class

        Args:
            *args - Unused argument.
            **kwargs - key/value pairs of attributes
        """

        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = self.updated_at = datetime.now()

        if kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if (key == "created_at") or (key == "updated_at"):
                    self.__dict__[key] = datetime.strptime(value, time_format)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """Update the attribute (updated_at) with current date and time."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return dictionary representation of superclass."""

        new = dict(self.__dict__)
        new["__class__"] = self.__class__.__name__
        new["created_at"] = self.created_at.isoformat()
        new["updated_at"] = self.updated_at.isoformat()
        return new

    def __str__(self):
        """Return string representation of superclass."""

        my_class = self.__class__.__name__
        return '[{}] ({}) {}'.format(my_class, self.id, self.__dict__)
