#!/usr/bin/python3
""" This is to testing files """
import unittest
from models.base_model import BaseModel
from datetime import datetime
import inspect
import pep8


class BaseModel_testing(unittest.TestCase):
    """ This is tocheck BaseModel """

    def testpep8(self):
        """ testing codestyle """
        pepstylecode = pep8.StyleGuide(quiet=True)
        rest = pepstylecode.check_files(['models/base_model.py',
                                         'models/__init__.py',
                                         'models/engine/file_storage.py'])
        self.assertEqual(rest.total_errors, 0,
                         "Found code style errors (and warnings).")


class test_for_base_model(unittest.TestCase):
    """This is to Class test for BaseModel """
    new_model = BaseModel()

    def TearDown(self):
        """ This is to delete json file """
        del self.test

    def SetUp(self):
        """ This is to Create instance """
        self.test = BaseModel()

    def test_attr_none(self):
        """ This is to None attribute."""
        object_test = BaseModel(None)
        self.assertTrue(hasattr(object_test, "id"))
        self.assertTrue(hasattr(object_test, "created_at"))
        self.assertTrue(hasattr(object_test, "updated_at"))

    def test_kwargs_constructor_2(self):
        """ This is to check id with data """
        new_dict = {'score': 100}

        object_test = BaseModel(**new_dict)
        self.assertTrue(hasattr(object_test, 'id'))
        self.assertTrue(hasattr(object_test, 'created_at'))
        self.assertTrue(hasattr(object_test, 'updated_at'))
        self.assertTrue(hasattr(object_test, 'score'))

    def test_str(self):
        """ This is to Test string """
        new_dict = {'id': 'cc9909cf-a909-9b90-9999-999fd99ca9a9',
                     'created_at': '2025-06-28T14:00:00.000001',
                     '__class__': 'BaseModel',
                     'updated_at': '2030-06-28T14:00:00.000001',
                     'score': 100
                     }

        object_test = BaseModel(**new_dict)
        out = "[{}] ({}) {}\n".format(type(object_test).__name__, object_test.id, object_test.__dict__)

    def test_to_dict(self):
        """ This is to check dict """
        object_test = BaseModel(score=300)
        n_diction = object_test.to_dict()

        self.assertEqual(n_diction['id'], object_test.id)
        self.assertEqual(n_diction['score'], 300)
        self.assertEqual(n_diction['__class__'], 'BaseModel')
        self.assertEqual(n_diction['created_at'], object_test.created_at.isoformat())
        self.assertEqual(n_diction['updated_at'], object_test.updated_at.isoformat())

        self.assertEqual(type(n_diction['created_at']), str)
        self.assertEqual(type(n_diction['created_at']), str)

    def test_datetime(self):
        """ This is to check datatime """
        bas4 = BaseModel()
        self.assertFalse(datetime.now() == bas4.created_at)

    def test_BaseModel(self):
        """ This is to check attributes values in a BaseModel """

        self.new_model.name = "Holbie"
        self.new_model.my_number = 100
        self.new_model.save()
        my_model_json = self.new_model.to_dict()

        self.assertEqual(self.new_model.name, my_model_json['name'])
        self.assertEqual(self.new_model.my_number, my_model_json['my_number'])
        self.assertEqual('BaseModel', my_model_json['__class__'])
        self.assertEqual(self.new_model.id, my_model_json['id'])

    def test_savefirst(self):
        """This is to check numbers"""
        with self.assertRaises(AttributeError):
            BaseModel.save([455, 323232, 2323, 2323, 23332])

    def test_savesecond(self):
        """ This is to check string """
        with self.assertRaises(AttributeError):
            BaseModel.save("THIS IS A TEST")

    def test_inst(self):
        """This is to check class """
        ml = BaseModel()
        self.assertTrue(ml, BaseModel)
