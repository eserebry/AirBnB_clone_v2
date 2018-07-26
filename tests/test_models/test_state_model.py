#!/usr/bin/python3
'''
    Contain tests for the state module.
'''
import os
import unittest
from models.base_model import BaseModel, Base
from models.state import State


class TestState(unittest.TestCase):
    '''
        Test the State class.
    '''

    def test_State_inheritence(self):
        '''
            Test that State class inherits from BaseModel.
        '''
        new_state = State()
        self.assertIsInstance(new_state, BaseModel)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', 'only FileStorage')
    def test_State_inheritance_Base(self):
        '''
            Test inheritance with declarative base
        '''
        new_state = State()
        self.assertIsInstance(new_state, Base)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', 'only FileStorage')
    def test_State_attributes(self):
        '''
            Test that State class contains the attribute `name`.
        '''
        new_state = State()
        self.assertTrue("name" in new_state.__dir__())

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', 'only FileStorage')
    def test_State_attributes_type(self):
        '''
            Test that State class attribute name is class type str.
        '''
        new_state = State()
        name = getattr(new_state, "name")
        self.assertIsInstance(name, str)


if __name__ == '__main__':
    unittest.main()
