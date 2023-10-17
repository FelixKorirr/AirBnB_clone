#!/usr/bin/python3
"""Define unittests for models/base_model.py.
"""
import os
import models
import unittest
from datetime import datetime
import time
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""

    def test_no_args(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_two_models_with_unique_ids(self):
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_created_at(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_two_models_with_different_created_at(self):
        model1 = BaseModel()
        time.sleep(0.05)
        model2 = BaseModel()
        self.assertLess(model1.created_at, model2.created_at)

    def test_updated_at(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_with_different_updated_at(self):
        model1 = BaseModel()
        time.sleep(0.05)
        model2 = BaseModel()
        self.assertLess(model1.updated_at, model2.updated_at)

    def test_str_repr(self):
        dte = datetime.today()
        dte_repr = repr(dte)
        model = BaseModel()
        model.id = "456789"
        model.created_at = model.updated_at = dte
        model_str = model.__str__()
        self.assertIn("[BaseModel] (456789)", model_str)
        self.assertIn("'id': '456789'", model_str)
        self.assertIn("'created_at': " + dte_repr, model_str)
        self.assertIn("'updated_at': " + dte_repr, model_str)

    def test_unused_args(self):
        model = BaseModel(None)
        self.assertNotIn(None, model.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dte = datetime.today()
        dte_iso = dte.isoformat()
        model = BaseModel(id="567", created_at=dte_iso, updated_at=dte_iso)
        self.assertEqual(model.id, "567")
        self.assertEqual(model.created_at, dte)
        self.assertEqual(model.updated_at, dte)

    def test_instantiation_without_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        dte = datetime.today()
        dte_iso = dte.isoformat()
        model = BaseModel("34", id="567",
                          created_at=dte_iso, updated_at=dte_iso)
        self.assertEqual(model.id, "567")
        self.assertEqual(model.created_at, dte)
        self.assertEqual(model.updated_at, dte)


class TestBaseModel_save(unittest.TestCase):
    """Unittest for testing save method of the BaseModel superclass."""

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

    def test_one_save(self):
        model = BaseModel()
        time.sleep(0.05)
        first_updated_at = model.updated_at
        model.save()
        self.assertLess(first_updated_at, model.updated_at)

    def test_two_saves(self):
        model = BaseModel()
        time.sleep(0.05)
        first_updated_at = model.updated_at
        model.save()
        second_updated_at = model.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        time.sleep(0.05)
        model.save()
        self.assertLess(second_updated_at, model.updated_at)

    def test_save_with_arg(self):
        model = BaseModel()
        with self.assertRaises(TypeError):
            model.save(None)

    def test_save_updates_file(self):
        model = BaseModel()
        model.save()
        model_id = "BaseModel." + model.id
        with open("file.json", "r") as file:
            self.assertIn(model_id, file.read())


class TestBaseModel_to_dict(unittest.TestCase):
    """Unittest for testing to_dict method of the BaseModel superclass."""

    def test_to_dict_type(self):
        model = BaseModel()
        self.assertTrue(dict, type(model.to_dict()))

    def test_to_dict_has_correct_keys(self):
        model = BaseModel()
        self.assertIn("id", model.to_dict())
        self.assertIn("created_at", model.to_dict())
        self.assertIn("updated_at", model.to_dict())
        self.assertIn("__class__", model.to_dict())

    def test_to_dict_datetime_attributes(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(str, type(model_dict["created_at"]))
        self.assertEqual(str, type(model_dict["updated_at"]))

    def test_to_dict_output(self):
        dte = datetime.today()
        model = BaseModel()
        model.id = "456789"
        model.created_at = model.updated_at = dte
        my_dict = {
            'id': '456789',
            '__class__': 'BaseModel',
            'created_at': dte.isoformat(),
            'updated_at': dte.isoformat()
        }
        self.assertDictEqual(model.to_dict(), my_dict)

    def test_to_dict_with_arg(self):
        model = BaseModel()
        with self.assertRaises(TypeError):
            model.to_dict(None)


if __name__ == "__main__":
    unittest.main()
