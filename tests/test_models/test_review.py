#!/usr/bin/python3
"""Define unittests for models/review.py."""
import os
import models
import unittest
from datetime import datetime
import time
from models.review import Review


class TestReview_instants(unittest.TestCase):
    """Unittests for testing instantiation of the Review class."""

    def test_no_args(self):
        self.assertEqual(Review, type(Review()))

    def test_new_instance(self):
        self.assertIn(Review(), models.storage.all().values())

    def test_id(self):
        self.assertEqual(str, type(Review().id))

    def test_created_at(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_place_id(self):
        rvw = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(rvw))
        self.assertNotIn("place_id", rvw.__dict__)

    def test_user_id(self):
        rvw = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(rvw))
        self.assertNotIn("user_id", rvw.__dict__)

    def test_text_is_public_class_attribute(self):
        rvw = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(rvw))
        self.assertNotIn("text", rvw.__dict__)

    def test_two_reviews_with_unique_ids(self):
        rvw1 = Review()
        rvw2 = Review()
        self.assertNotEqual(rvw1.id, rvw2.id)

    def test_two_reviews_with_different_created_at(self):
        rvw1 = Review()
        time.sleep(0.05)
        rvw2 = Review()
        self.assertLess(rvw1.created_at, rvw2.created_at)

    def test_two_reviews_with_different_updated_at(self):
        rvw1 = Review()
        time.sleep(0.05)
        rvw2 = Review()
        self.assertLess(rvw1.updated_at, rvw2.updated_at)

    def test_str_repr(self):
        dte = datetime.today()
        dte_repr = repr(dte)
        rvw = Review()
        rvw.id = "456789"
        rvw.created_at = rvw.updated_at = dte
        rvw_str = rvw.__str__()
        self.assertIn("[Review] (456789)", rvw_str)
        self.assertIn("'id': '456789'", rvw_str)
        self.assertIn("'created_at': " + dte_repr, rvw_str)
        self.assertIn("'updated_at': " + dte_repr, rvw_str)

    def test_unused_args(self):
        rvw = Review(None)
        self.assertNotIn(None, rvw.__dict__.values())

    def test_instants_with_kwargs(self):
        dte = datetime.today()
        dte_iso = dte.isoformat()
        rvw = Review(id="123", created_at=dte_iso, updated_at=dte_iso)
        self.assertEqual(rvw.id, "123")
        self.assertEqual(rvw.created_at, dte)
        self.assertEqual(rvw.updated_at, dte)

    def test_instants_without_kwargs(self):
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)


class TestReview_save(unittest.TestCase):
    """Unittests for testing save method of the Review class."""

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
        rvw = Review()
        time.sleep(0.05)
        first_updated_at = rvw.updated_at
        rvw.save()
        self.assertLess(first_updated_at, rvw.updated_at)

    def test_two_saves(self):
        rvw = Review()
        time.sleep(0.05)
        first_updated_at = rvw.updated_at
        rvw.save()
        second_updated_at = rvw.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        time.sleep(0.05)
        rvw.save()
        self.assertLess(second_updated_at, rvw.updated_at)

    def test_save_with_args(self):
        rvw = Review()
        with self.assertRaises(TypeError):
            rvw.save(None)

    def test_save_updates(self):
        rvw = Review()
        rvw.save()
        rvw_id = "Review." + rvw.id
        with open("file.json", "r") as file:
            self.assertIn(rvw_id, file.read())


class TestReview_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the Review class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Review().to_dict()))

    def test_to_dict_has_right_keys(self):
        rvw = Review()
        self.assertIn("id", rvw.to_dict())
        self.assertIn("created_at", rvw.to_dict())
        self.assertIn("updated_at", rvw.to_dict())
        self.assertIn("__class__", rvw.to_dict())

    def test_to_dict_has_added_attributes(self):
        rvw = Review()
        rvw.middle_name = "ALX"
        rvw.my_number = 89
        self.assertEqual("ALX", rvw.middle_name)
        self.assertIn("my_number", rvw.to_dict())

    def test_to_dict_datetime_attributes(self):
        rvw = Review()
        rvw_dict = rvw.to_dict()
        self.assertEqual(str, type(rvw_dict["id"]))
        self.assertEqual(str, type(rvw_dict["created_at"]))
        self.assertEqual(str, type(rvw_dict["updated_at"]))

    def test_to_dict_output(self):
        dte = datetime.today()
        rvw = Review()
        rvw.id = "456789"
        rvw.created_at = rvw.updated_at = dte
        my_dict = {
            'id': '456789',
            '__class__': 'Review',
            'created_at': dte.isoformat(),
            'updated_at': dte.isoformat(),
        }
        self.assertDictEqual(rvw.to_dict(), my_dict)

    def test_to_dict_with_arg(self):
        rvw = Review()
        with self.assertRaises(TypeError):
            rvw.to_dict(None)


if __name__ == "__main__":
    unittest.main()
