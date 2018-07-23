#!/usr/bin/python3
'''
    Implementation of the State class
'''
import sqlalchemy
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String

class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete-orphan")
