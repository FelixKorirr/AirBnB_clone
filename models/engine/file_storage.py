#!/usr/bin/python3
"""Define superclass FileStorage."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represent the new class."""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects the obj with key."""
        class_name = obj.__class__.__name__
        key = "{}.{}".format(class_name, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to JSOn file."""
        serialized_data = {}
        for key, value in FileStorage.__objects.items():
            serialized_data[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w') as file:
            json_data = json.dumps(serialized_data)
            file.write(json_data)

    def reload(self):
        """Deserialize JSOn file to __objects"""
        try:
            with open(FileStorage.__file_path) as file:
                obj_dict = json.load(file)
                for i in obj_dict.values():
                    class_name = i["__class__"]
                    del i["__class__"]
                    self.new(eval(class_name)(**i))
        except FileNotFoundError:
            pass
