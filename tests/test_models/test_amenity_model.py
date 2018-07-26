#!/usr/bin/python3

'''
    All the test for the amenity model are implemented here.
'''
import os
import unittest
from models.base_model import BaseModel, Base
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    '''
        Testing Amenity class
    '''

    def test_Amenity_inheritence(self):
        '''
            tests that the Amenity class Inherits from BaseModel
        '''
        new_amenity = Amenity()
        self.assertIsInstance(new_amenity, BaseModel)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', 'only FileStorage')
    def test_Amenity_inheritance_Base(self):
        '''
            test inheritance with declarative base
        '''
        new_amenity = Amenity()
        self.assertIsInstance(new_amenity, Base)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', 'only FileStorage')
    def test_Amenity_attributes(self):
        '''
            Test that Amenity class had name attribute.
        '''
        new_amenity = Amenity()
        self.assertTrue("name" in new_amenity.__dir__())

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', 'only FileStorage')
    def test_Amenity_attribute_type(self):
        '''
            Test that Amenity class had name attribute's type.
        '''
        new_amenity = Amenity()
        name_value = getattr(new_amenity, "name")
        self.assertIsInstance(name_value, str)


if __name__ == '__main__':
    unittest.main()
