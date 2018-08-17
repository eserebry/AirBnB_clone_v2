#!/usr/bin/python3
'''
    Implementation of the State class
'''
import sqlalchemy
import models
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from os import getenv
from models.city import City


class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''
    __tablename__ = 'states'
    if getenv('HBNB_TYPE_STORAGE') == 'db':

        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete-orphan")

    else:
        name = ""

        @property
        def cities(self):
            instance_list = []
            for key, obj in models.storage.all(City).items():
                if obj.state_id == self.id:
                    instance_list.append(obj)
            return instance_list
