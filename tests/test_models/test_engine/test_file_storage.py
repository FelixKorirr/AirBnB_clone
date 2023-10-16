#!/usr/bin/python3
"""Define unittests for models/engine/file_storage.py."""

import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place


class TestFileStorage_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the FileStorage class."""

    def test_FileStorage_instants__with_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instants_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_storage(self):
        self.assertEqual(type(models.storage), FileStorage)

    def test_FileStorage_file_path(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))


class TestFileStorage_methods(unittest.TestCase):
    """Unittests for testing methods of the FileStorage class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "x")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("x", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all_method(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_method_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new_method(self):
        mod = BaseModel()
        usr = User()
        stat = State()
        plc = Place()
        cty = City()
        amt = Amenity()
        rv = Review()
        models.storage.new(mod)
        models.storage.new(usr)
        models.storage.new(stat)
        models.storage.new(plc)
        models.storage.new(cty)
        models.storage.new(amt)
        models.storage.new(rv)
        self.assertIn("BaseModel." + mod.id, models.storage.all().keys())
        self.assertIn(mod, models.storage.all().values())
        self.assertIn("User." + usr.id, models.storage.all().keys())
        self.assertIn(usr, models.storage.all().values())
        self.assertIn("State." + stat.id, models.storage.all().keys())
        self.assertIn(stat, models.storage.all().values())
        self.assertIn("Place." + plc.id, models.storage.all().keys())
        self.assertIn(plc, models.storage.all().values())
        self.assertIn("City." + cty.id, models.storage.all().keys())
        self.assertIn(cty, models.storage.all().values())
        self.assertIn("Amenity." + amt.id, models.storage.all().keys())
        self.assertIn(amt, models.storage.all().values())
        self.assertIn("Review." + rv.id, models.storage.all().keys())
        self.assertIn(rv, models.storage.all().values())

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_save_method(self):
        mod = BaseModel()
        usr = User()
        stat = State()
        plc = Place()
        cty = City()
        amt = Amenity()
        rv = Review()
        models.storage.new(mod)
        models.storage.new(usr)
        models.storage.new(stat)
        models.storage.new(plc)
        models.storage.new(cty)
        models.storage.new(amt)
        models.storage.new(rv)
        models.storage.save()
        saved_txt = ""
        with open("file.json", "r") as file:
            saved_txt = file.read()
            self.assertIn("BaseModel." + mod.id, saved_txt)
            self.assertIn("User." + usr.id, saved_txt)
            self.assertIn("State." + stat.id, saved_txt)
            self.assertIn("Place." + plc.id, saved_txt)
            self.assertIn("City." + cty.id, saved_txt)
            self.assertIn("Amenity." + amt.id, saved_txt)
            self.assertIn("Review." + rv.id, saved_txt)

    def test_save_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        mod = BaseModel()
        usr = User()
        stat = State()
        plc = Place()
        cty = City()
        amt = Amenity()
        rv = Review()
        models.storage.new(mod)
        models.storage.new(usr)
        models.storage.new(stat)
        models.storage.new(plc)
        models.storage.new(cty)
        models.storage.new(amt)
        models.storage.new(rv)
        models.storage.save()
        models.storage.reload()
        obj = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + mod.id, obj)
        self.assertIn("User." + usr.id, obj)
        self.assertIn("State." + stat.id, obj)
        self.assertIn("Place." + plc.id, obj)
        self.assertIn("City." + cty.id, obj)
        self.assertIn("Amenity." + amt.id, obj)
        self.assertIn("Review." + rv.id, obj)

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
