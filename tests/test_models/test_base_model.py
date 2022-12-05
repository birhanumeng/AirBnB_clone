#!/usr/bin/python3

"""
Module containing unittest for BaseModel
"""

import os
import unittest
import models
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class Test_BaseModel_instantiation(unittest.TestCase):
    """Tesing the creation/instantiation of the
    Basemodel class or its objects"""

    def setUp(self):
        """Setting up objects to be used to run the tests"""
        self.base_1 = BaseModel()
        self.base_2 = BaseModel()

    def tearDown(self):
        """Remove resources that where used to run tests"""
        del self.base_1
        del self.base_2

    def test_unique_IDs(self):
        """Test that two objects of BaseModel class have different id's"""
        self.assertNotEqual(self.base_1.id, self.base_2.id)

    def test_id_is_public_str(self):
        """Test that the id is in sting format"""
        self.assertEqual(str, type(self.base_1.id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(self.base_1.created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_different_created_at(self):
        """Test to make sure two objects where created at separate times"""
        base1 = BaseModel()
        sleep(0.05)
        base2 = BaseModel()
        self.assertLess(base1.created_at, base2.created_at)

    def test_two_models_different_updated_at(self):
        base1 = BaseModel()
        sleep(0.05)
        base2 = BaseModel()
        self.assertLess(base1.updated_at, base2.updated_at)

    def test_kwargs_initialization(self):
        """Test the initialization of a class using kwargs"""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        base = BaseModel(id="6453", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(base.id, "6453")
        self.assertEqul(base.created_at, dt)
        self.assertEqual(base.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_args_unused(self):
        base = BaseModel(None)
        self.assertNotIn(None, base.__dict__.values())

    def test_str(self):
        """Test str method present in BaseModel class"""
        base2 = BaseModel()
        self.assertIn("id", base2.__str__())
        self.assertIn("created_at", base2.__str__())
        self.assertIn("updated_at", base2.__str__())
        self.assertIn("[BaseModel]", base2.__str__())
        self.assertTrue(type(base2.__str__()), str)
        self.assertIsNotNone(base2.__str__())

    def test_to_dict(self):
        """Test the return value of the to_dict() method"""
        test_dict = {key: value for key, value in self.base_1.__dict__.items()}
        test_dict['created_at'] = self.base_1.created_at.isoformat()
        test_dict['updated_at'] = self.base_1.updated_at.isoformat()
        test_dict['__class__'] = type(self.base_1).__name__
        self.assertEqual(self.base_1.to_dict(), test_dict)


if __name__ == '__main__':
    unittest.main()
