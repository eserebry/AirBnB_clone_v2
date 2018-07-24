#!/usr/bin/python3
'''
    Implementation of the Amenity class
'''
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String
from os import getenv
from sqlalchemy.orm import relationship

class Amenity(BaseModel, Base):
    '''
        Implementation for the Amenities.
    '''
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
        place_amenities = relationship()

    else:
        name = ""
