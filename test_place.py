#!/usr/bin/python3
""" testing Place """
import unittest
import pep8
from models.place import Place

class Place_testing(unittest.TestCase):
    """ check BaseModel """

    def testpep8(self):
        """ testing codestyle """
        pepstylecodes = pep8.StyleGuide(quiet=True)
        user_paths = 'models/place.py'
        outcomes = pepstylecodes.check_files([user_paths])
        self.assertEqual(outcomes.total_errors, 0,
                         "Found code style errors (and warnings).")
