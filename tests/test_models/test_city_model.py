#!/usr/bin/python3

'''
    All the test for the user model are implemented here.
'''
import os
import unittest
from models.base_model import BaseModel, Base
from models.city import City


class TestUser(unittest.TestCase):
    '''
        Testing User class
    '''

    def test_City_inheritance(self):
        '''
            tests that the City class Inherits from BaseModel
        '''
        new_city = City()
        self.assertIsInstance(new_city, BaseModel)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', 'only FileStorage')
    def test_City_inheritance_Base(self):
        '''
            tests the inheritance with declarative base
        '''
        new_city = City()
        self.assertIsInstance(new_city, Base)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', 'only FileStorage')
    def test_User_attributes(self):
        new_city = City()
        self.assertTrue("state_id" in new_city.__dir__())
        self.assertTrue("name" in new_city.__dir__())

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', 'only FileStorage')
    def test_type_name(self):
        '''
            Test the type of name
        '''
        new_city = City()
        name = getattr(new_city, "name")
        self.assertIsInstance(name, str)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', 'only FileStorage')
    def test_type_name(self):
        '''
            Test the type of name
        '''
        new_city = City()
        name = getattr(new_city, "state_id")
        self.assertIsInstance(name, str)


if __name__ == '__main__':
    unittest.main()
