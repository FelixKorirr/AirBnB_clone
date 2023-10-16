#!/usr/bin/python3
"""Contains the class TestConsole_Docs"""

import console
import inspect
import pep8
import unittest
HBNBCommand = console.HBNBCommand


class TestConsole_Docs(unittest.TestCase):
    """Class for testing documentation of the console"""

    def test_pep8_conformance_console(self):
        """Test if command interpreter conforms to PEP8."""
        peps = pep8.StyleGuide(quiet=True)
        result = peps.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                        "Found code style errors (and warnings).")

    def test_pep8_conformance_on_test(self):
        """Test if test_console.py conforms to PEP8."""
        peps = pep8.StyleGuide(quiet=True)
        reslt = peps.check_files(['tests/test_console.py'])
        self.assertEqual(reslt.total_errors, 0,
                        "Found code style errors (and warnings).")

    def test_console_docstring(self):
        """Test for the console.py module docstring"""
        self.assertIsNot(console.__doc__, None,
                         "console.py needs a docstring")
        self.assertTrue(len(console.__doc__) >= 1,
                        "console.py needs a docstring")

    def test_HBNBCommand_class_docstring(self):
        """Test for the HBNBCommand class docstring"""
        self.assertIsNot(HBNBCommand.__doc__, None,
                        "HBNBCommand class needs a docstring")
        self.assertTrue(len(HBNBCommand.__doc__) >= 1,
                        "HBNBCommand class needs a docstring")
