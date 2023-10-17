#!/usr/bin/python3
"""Defines unittests for models/state.py."""
import os
import models
import unittest
from datetime import datetime
import time
from models.state import State


class TestState_instants(unittest.TestCase):
    """Unittests for testing instantiation of the State class."""

    def test_no_args(self):
        self.assertEqual(State, type(State()))

    def test_new_instance(self):
        self.assertIn(State(), models.storage.all().values())

    def test_id(self):
        self.assertEqual(str, type(State().id))

    def test_created_at(self):
        self.assertEqual(datetime, type(State().created_at))

    def test_updated_at(self):
        self.assertEqual(datetime, type(State().updated_at))

    def test_two_states_with_unique_ids(self):
        str1 = State()
        str2 = State()
        self.assertNotEqual(str1.id, str2.id)

    def test_two_states_with_different_created_at(self):
        str1 = State()
        time.sleep(0.05)
        str2 = State()
        self.assertLess(str1.created_at, str2.created_at)

    def test_two_states_with_different_updated_at(self):
        str1 = State()
        time.sleep(0.05)
        str2 = State()
        self.assertLess(str1.updated_at, str2.updated_at)

    def test_str_repr(self):
        dte = datetime.today()
        dte_repr = repr(dte)
        str = State()
        str.id = "456789"
        str.created_at = str.updated_at = dte
        ststr = str.__str__()
        self.assertIn("[State] (456789)", ststr)
        self.assertIn("'id': '456789'", ststr)
        self.assertIn("'created_at': " + dte_repr, ststr)
        self.assertIn("'updated_at': " + dte_repr, ststr)

    def test_unused_args(self):
        str = State(None)
        self.assertNotIn(None, str.__dict__.values())

    def test_instants_with_kwargs(self):
        dte = datetime.today()
        dte_iso = dte.isoformat()
        str = State(id="123", created_at=dte_iso, updated_at=dte_iso)
        self.assertEqual(str.id, "123")
        self.assertEqual(str.created_at, dte)
        self.assertEqual(str.updated_at, dte)

    def test_instants_without_kwargs(self):
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)


class TestState_save(unittest.TestCase):
    """Unittests for testing save method of State class."""

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
        str = State()
        time.sleep(0.05)
        first_updated_at = str.updated_at
        str.save()
        self.assertLess(first_updated_at, str.updated_at)

    def test_two_saves(self):
        str = State()
        time.sleep(0.05)
        first_updated_at = str.updated_at
        str.save()
        second_updated_at = str.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        time.sleep(0.05)
        str.save()
        self.assertLess(second_updated_at, str.updated_at)

    def test_save_with_args(self):
        str = State()
        with self.assertRaises(TypeError):
            str.save(None)

    def test_save_updates(self):
        str = State()
        str.save()
        str_id = "State." + str.id
        with open("file.json", "r") as file:
            self.assertIn(str_id, file.read())


class TestState_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the State class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(State().to_dict()))

    def test_to_dict_has_keys(self):
        str = State()
        self.assertIn("id", str.to_dict())
        self.assertIn("created_at", str.to_dict())
        self.assertIn("updated_at", str.to_dict())
        self.assertIn("__class__", str.to_dict())

    def test_to_dict_has_added_attributes(self):
        str = State()
        str.middle_name = "ALX"
        str.my_number = 89
        self.assertEqual("ALX", str.middle_name)
        self.assertIn("my_number", str.to_dict())

    def test_to_dict_output(self):
        dte = datetime.today()
        str = State()
        str.id = "456789"
        str.created_at = str.updated_at = dte
        my_dict = {
            'id': '456789',
            '__class__': 'State',
            'created_at': dte.isoformat(),
            'updated_at': dte.isoformat(),
        }
        self.assertDictEqual(str.to_dict(), my_dict)

    def test_to_dict_with_args(self):
        str = State()
        with self.assertRaises(TypeError):
            str.to_dict(None)


if __name__ == "__main__":
    unittest.main()
