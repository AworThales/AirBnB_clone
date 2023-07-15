#!/usr/bin/python3
""" This is to testing User """
import unittest
import pep8
from models.user import User

class User_testing(unittest.TestCase):
    """ This is to check BaseModel """

    def testpep8(self):
        """ This is to testing codestyle """
        pepstylecode = pep8.StyleGuide(quiet=True)
        user_paths = 'models/user.py'
        outcomes = pepstylecode.check_files([user_paths])
        self.assertEqual(outcomes.total_errors, 0,
                         "Found code style errors (and warnings).")
