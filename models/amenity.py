#!/usr/bin/python3
'''
    Implementation of the Amenity class
'''
from models.base_model import BaseModel
import sqlalchemy
from sqlalchemy import Column, String
from os import getenv

class Amenity(BaseModel):
    '''
        Implementation for the Amenities.
    '''
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)

    else:
        name = ""
