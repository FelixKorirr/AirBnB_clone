#!/usr/bin/python3
"""Defines unittests for models/user.py."""
import os
import models
import unittest
from datetime import datetime
import time
from models.user import User


class TestUser_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the User class."""

    def test_no_args(self):
        self.assertEqual(User, type(User()))

    def test_new_instance(self):
        self.assertIn(User(), models.storage.all().values())

    def test_id(self):
        self.assertEqual(str, type(User().id))

    def test_created_at(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_email(self):
        self.assertEqual(str, type(User.email))

    def test_password(self):
        self.assertEqual(str, type(User.password))

    def test_first_name(self):
        self.assertEqual(str, type(User.first_name))

    def test_last_name(self):
        self.assertEqual(str, type(User.last_name))

    def test_two_users_with_unique_ids(self):
        usr1 = User()
        usr2 = User()
        self.assertNotEqual(usr1.id, usr2.id)

    def test_two_users_with_different_created_at(self):
        usr1 = User()
        time.sleep(0.05)
        usr2 = User()
        self.assertLess(usr1.created_at, usr2.created_at)

    def test_two_users_with_different_updated_at(self):
        usr1 = User()
        time.sleep(0.05)
        usr2 = User()
        self.assertLess(usr1.updated_at, usr2.updated_at)

    def test_str_repr(self):
        dte = datetime.today()
        dte_repr = repr(dte)
        usr = User()
        usr.id = "456789"
        usr.created_at = usr.updated_at = dte
        usr_str = usr.__str__()
        self.assertIn("[User] (456789)", usr_str)
        self.assertIn("'id': '456789'", usr_str)
        self.assertIn("'created_at': " + dte_repr, usr_str)
        self.assertIn("'updated_at': " + dte_repr, usr_str)

    def test_unused_args(self):
        usr = User(None)
        self.assertNotIn(None, usr.__dict__.values())

    def test_instants_with_kwargs(self):
        dte = datetime.today()
        dte_iso = dte.isoformat()
        usr = User(id="123", created_at=dte_iso, updated_at=dte_iso)
        self.assertEqual(usr.id, "123")
        self.assertEqual(usr.created_at, dte)
        self.assertEqual(usr.updated_at, dte)

    def test_instants_without_kwargs(self):
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)


class TestUser_save(unittest.TestCase):
    """Unittests for testing save method of the  class."""

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
        usr = User()
        time.sleep(0.05)
        first_updated_at = usr.updated_at
        usr.save()
        self.assertLess(first_updated_at, usr.updated_at)

    def test_two_saves(self):
        usr = User()
        time.sleep(0.05)
        first_updated_at = usr.updated_at
        usr.save()
        second_updated_at = usr.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        time.sleep(0.05)
        usr.save()
        self.assertLess(second_updated_at, usr.updated_at)

    def test_save_with_args(self):
        usr = User()
        with self.assertRaises(TypeError):
            usr.save(None)

    def test_save_updates(self):
        usr = User()
        usr.save()
        usr_id = "User." + usr.id
        with open("file.json", "r") as file:
            self.assertIn(usr_id, file.read())


class TestUser_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the User class."""

    def test_to_dict_method(self):
        self.assertTrue(dict, type(User().to_dict()))

    def test_to_dict_keys(self):
        usr = User()
        self.assertIn("id", usr.to_dict())
        self.assertIn("created_at", usr.to_dict())
        self.assertIn("updated_at", usr.to_dict())
        self.assertIn("__class__", usr.to_dict())

    def test_to_dict_contains_added_attributes(self):
        usr = User()
        usr.middle_name = "ALX"
        usr.my_number = 89
        self.assertEqual("ALX", usr.middle_name)
        self.assertIn("my_number", usr.to_dict())

    def test_to_dict_datetime_attributes(self):
        usr = User()
        usr_dict = usr.to_dict()
        self.assertEqual(str, type(usr_dict["id"]))
        self.assertEqual(str, type(usr_dict["created_at"]))
        self.assertEqual(str, type(usr_dict["updated_at"]))

    def test_to_dict_output(self):
        dte = datetime.today()
        usr = User()
        usr.id = "456789"
        usr.created_at = usr.updated_at = dte
        my_dict = {
            'id': '456789',
            '__class__': 'User',
            'created_at': dte.isoformat(),
            'updated_at': dte.isoformat(),
        }
        self.assertDictEqual(usr.to_dict(), my_dict)

    def test_to_dict_with_args(self):
        usr = User()
        with self.assertRaises(TypeError):
            usr.to_dict(None)


if __name__ == "__main__":
    unittest.main()
