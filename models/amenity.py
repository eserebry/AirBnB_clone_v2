#!/usr/bin/python3
'''
    Implementation of the Amenity class
'''
from models.base_model import BaseModel
import sqlalchemy
from sqlalchemy import Column, String

class Amenity(BaseModel):
    '''
        Implementation for the Amenities.
    '''

    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)
