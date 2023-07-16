#!/usr/bin/python3
""" This is to testing Review """
import unittest
import pep8
from models.review import Review

class Review_testing(unittest.TestCase):
    """ This is to check BaseModel """

    def testpep8(self):
        """ This is to testing codestyle """
        pepstylecodes = pep8.StyleGuide(quiet=True)
        user_paths = 'models/review.py'
        outcome = pepstylecodes.check_files([user_paths])
        self.assertEqual(outcome.total_errors, 0,
                         "Found code style errors (and warnings).")
