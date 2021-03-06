#!/usr/bin/python3
'''
    Implementation of the User class which inherits from BaseModel
'''
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class User(BaseModel, Base):
    '''
        Definition of the User class
    '''
    __tablename__ = 'users'

    if getenv('HBNB_TYPE_STORAGE') == 'db':

        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", cascade="all, delete-orphan")
        reviews = relationship("Review", cascade="all, delete-orphan")

    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
