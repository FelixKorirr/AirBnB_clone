#!/usr/bin/python3
"""Defines unittests for models/amenity.py."""
import os
import models
import unittest
from datetime import datetime
import time
from models.amenity import Amenity


class TestAmenity_instants(unittest.TestCase):
    """Unittests for testing instantiation of the Amenity class."""

    def test_no_args(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_instance(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_at(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name_is_public_class_attribute(self):
        amty = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", amty.__dict__)

    def test_two_amenities_with_unique_ids(self):
        amty1 = Amenity()
        amty2 = Amenity()
        self.assertNotEqual(amty1.id, amty2.id)

    def test_two_amenities_with_different_created_at(self):
        amty1 = Amenity()
        time.sleep(0.05)
        amty2 = Amenity()
        self.assertLess(amty1.created_at, amty2.created_at)

    def test_two_amenities_with_different_updated_at(self):
        amty1 = Amenity()
        time.sleep(0.05)
        amty2 = Amenity()
        self.assertLess(amty1.updated_at, amty2.updated_at)

    def test_str_repr(self):
        dte = datetime.today()
        dte_repr = repr(dte)
        amty = Amenity()
        amty.id = "456789"
        amty.created_at = amty.updated_at = dte
        amty_str = amty.__str__()
        self.assertIn("[Amenity] (456789)", amty_str)
        self.assertIn("'id': '456789'", amty_str)
        self.assertIn("'created_at': " + dte_repr, amty_str)
        self.assertIn("'updated_at': " + dte_repr, amty_str)

    def test_unused_args(self):
        amty = Amenity(None)
        self.assertNotIn(None, amty.__dict__.values())

    def test_instants_with_kwargs(self):
        dte = datetime.today()
        dte_iso = dte.isoformat()
        amty = Amenity(id="123", created_at=dte_iso, updated_at=dte_iso)
        self.assertEqual(amty.id, "123")
        self.assertEqual(amty.created_at, dte)
        self.assertEqual(amty.updated_at, dte)

    def test_instants_without_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)


class TestAmenity_save(unittest.TestCase):
    """Unittests for testing save method of the Amenity class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "x")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("x", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        amty = Amenity()
        time.sleep(0.05)
        first_updated_at = amty.updated_at
        amty.save()
        self.assertLess(first_updated_at, amty.updated_at)

    def test_two_saves(self):
        amty = Amenity()
        time.sleep(0.05)
        first_updated_at = amty.updated_at
        amty.save()
        second_updated_at = amty.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        time.sleep(0.05)
        amty.save()
        self.assertLess(second_updated_at, amty.updated_at)

    def test_save_with_args(self):
        amty = Amenity()
        with self.assertRaises(TypeError):
            amty.save(None)

    def test_save_updates(self):
        amty = Amenity()
        amty.save()
        amty_id = "Amenity." + amty.id
        with open("file.json", "r") as file:
            self.assertIn(amty_id, file.read())


class TestAmenity_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the Amenity class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_to_dict_has_keys(self):
        amty = Amenity()
        self.assertIn("id", amty.to_dict())
        self.assertIn("created_at", amty.to_dict())
        self.assertIn("updated_at", amty.to_dict())
        self.assertIn("__class__", amty.to_dict())

    def test_to_dict_has_added_attributes(self):
        amty = Amenity()
        amty.middle_name = "ALX"
        amty.my_number = 89
        self.assertEqual("ALX", amty.middle_name)
        self.assertIn("my_number", amty.to_dict())

    def test_to_dict_datetime_attributes(self):
        amty = Amenity()
        am_dict = amty.to_dict()
        self.assertEqual(str, type(am_dict["id"]))
        self.assertEqual(str, type(am_dict["created_at"]))
        self.assertEqual(str, type(am_dict["updated_at"]))

    def test_to_dict_output(self):
        dte = datetime.today()
        amty = Amenity()
        amty.id = "456789"
        amty.created_at = amty.updated_at = dte
        tdict = {
            'id': '456789',
            '__class__': 'Amenity',
            'created_at': dte.isoformat(),
            'updated_at': dte.isoformat(),
        }
        self.assertDictEqual(amty.to_dict(), tdict)

    def test_to_dict_with_arg(self):
        amty = Amenity()
        with self.assertRaises(TypeError):
            amty.to_dict(None)


if __name__ == "__main__":
    unittest.main()
