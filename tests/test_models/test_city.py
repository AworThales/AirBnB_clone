#!/usr/bin/python3
"""This is to testing city """
import unittest
import pep8
from models.city import City

class City_testing(unittest.TestCase):
    """This is to check BaseModel """

    def testpep8(self):
        """ This is to testing codestyle """
        pepstylecodes = pep8.StyleGuide(quiet=True)
        user_paths = 'models/city.py'
        outcomes = pepstylecodes.check_files([user_paths])
        self.assertEqual(outcomes.total_errors, 0,
                         "Found code style errors (and warnings).")
