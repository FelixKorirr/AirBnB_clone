#!/usr/bin/python3
"""Defines unittests for models/place.py."""
import os
import models
import unittest
from datetime import datetime
import time
from models.place import Place


class TestPlace_instants(unittest.TestCase):
    """Unittests for testing instantiation of the Place class."""

    def test_no_args(self):
        self.assertEqual(Place, type(Place()))

    def test_new_instance(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_id(self):
        self.assertEqual(str, type(Place().id))

    def test_created_at(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_city_id(self):
        plc = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(plc))
        self.assertNotIn("city_id", plc.__dict__)

    def test_user_id(self):
        plc = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(plc))
        self.assertNotIn("user_id", plc.__dict__)

    def test_name(self):
        plc = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(plc))
        self.assertNotIn("name", plc.__dict__)

    def test_description(self):
        plc = Place()
        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(plc))
        self.assertNotIn("desctiption", plc.__dict__)

    def test_number_rooms(self):
        plc = Place()
        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(plc))
        self.assertNotIn("number_rooms", plc.__dict__)

    def test_number_of_bathrooms(self):
        plc = Place()
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertIn("number_bathrooms", dir(plc))
        self.assertNotIn("number_bathrooms", plc.__dict__)

    def test_max_no_of_guest(self):
        plc = Place()
        self.assertEqual(int, type(Place.max_guest))
        self.assertIn("max_guest", dir(plc))
        self.assertNotIn("max_guest", plc.__dict__)

    def test_price_by_night(self):
        plc = Place()
        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(plc))
        self.assertNotIn("price_by_night", plc.__dict__)

    def test_latitude(self):
        plc = Place()
        self.assertEqual(float, type(Place.latitude))
        self.assertIn("latitude", dir(plc))
        self.assertNotIn("latitude", plc.__dict__)

    def test_longitude(self):
        plc = Place()
        self.assertEqual(float, type(Place.longitude))
        self.assertIn("longitude", dir(plc))
        self.assertNotIn("longitude", plc.__dict__)

    def test_amenity_ids(self):
        plc = Place()
        self.assertEqual(list, type(Place.amenity_ids))
        self.assertIn("amenity_ids", dir(plc))
        self.assertNotIn("amenity_ids", plc.__dict__)

    def test_two_places_with_unique_ids(self):
        plc1 = Place()
        plc2 = Place()
        self.assertNotEqual(plc1.id, plc2.id)

    def test_two_places_with_different_created_at(self):
        plc1 = Place()
        time.sleep(0.05)
        plc2 = Place()
        self.assertLess(plc1.created_at, plc2.created_at)

    def test_two_places_with_different_updated_at(self):
        plc1 = Place()
        time.sleep(0.05)
        plc2 = Place()
        self.assertLess(plc1.updated_at, plc2.updated_at)

    def test_str_repr(self):
        dte = datetime.today()
        dte_repr = repr(dte)
        plc = Place()
        plc.id = "456789"
        plc.created_at = plc.updated_at = dte
        plc_str = plc.__str__()
        self.assertIn("[Place] (456789)", plc_str)
        self.assertIn("'id': '456789'", plc_str)
        self.assertIn("'created_at': " + dte_repr, plc_str)
        self.assertIn("'updated_at': " + dte_repr, plc_str)

    def test_unused_args(self):
        plc = Place(None)
        self.assertNotIn(None, plc.__dict__.values())

    def test_instants_with_kwargs(self):
        dte = datetime.today()
        dte_iso = dte.isoformat()
        plc = Place(id="123", created_at=dte_iso, updated_at=dte_iso)
        self.assertEqual(plc.id, "123")
        self.assertEqual(plc.created_at, dte)
        self.assertEqual(plc.updated_at, dte)

    def test_instants_without_kwargs(self):
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)


class TestPlace_save(unittest.TestCase):
    """Unittests for testing save method of the Place class."""

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
        plc = Place()
        time.sleep(0.05)
        first_updated_at = plc.updated_at
        plc.save()
        self.assertLess(first_updated_at, plc.updated_at)

    def test_two_saves(self):
        plc = Place()
        time.sleep(0.05)
        first_updated_at = plc.updated_at
        plc.save()
        second_updated_at = plc.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        time.sleep(0.05)
        plc.save()
        self.assertLess(second_updated_at, plc.updated_at)

    def test_save_with_args(self):
        plc = Place()
        with self.assertRaises(TypeError):
            plc.save(None)

    def test_save_updates(self):
        plc = Place()
        plc.save()
        plc_id = "Place." + plc.id
        with open("file.json", "r") as file:
            self.assertIn(plc_id, file.read())


class TestPlace_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the Place class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Place().to_dict()))

    def test_to_dict_has_keys(self):
        plc = Place()
        self.assertIn("id", plc.to_dict())
        self.assertIn("created_at", plc.to_dict())
        self.assertIn("updated_at", plc.to_dict())
        self.assertIn("__class__", plc.to_dict())

    def test_to_dict_has_added_attributes(self):
        plc = Place()
        plc.middle_name = "ALX"
        plc.my_number = 89
        self.assertEqual("ALX", plc.middle_name)
        self.assertIn("my_number", plc.to_dict())

    def test_to_dict_datetime_attributes(self):
        plc = Place()
        plc_dict = plc.to_dict()
        self.assertEqual(str, type(plc_dict["id"]))
        self.assertEqual(str, type(plc_dict["created_at"]))
        self.assertEqual(str, type(plc_dict["updated_at"]))

    def test_to_dict_output(self):
        dte = datetime.today()
        plc = Place()
        plc.id = "123456"
        plc.created_at = plc.updated_at = dte
        my_dict = {
            'id': '123456',
            '__class__': 'Place',
            'created_at': dte.isoformat(),
            'updated_at': dte.isoformat(),
        }
        self.assertDictEqual(plc.to_dict(), my_dict)

    def test_to_dict_with_arg(self):
        plc = Place()
        with self.assertRaises(TypeError):
            plc.to_dict(None)


if __name__ == "__main__":
    unittest.main()
