#!/usr/bin/python3
'''
    Implementation of the Review class
'''
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from os import getenv
from sqlalchemy.orm import relationship

class Review(BaseModel, Base):
    '''
        Implementation for the Review.
    '''
    __tablename__ = 'reviews'
    if getenv('HBNB_TYPE_STORAGE') == 'db':

        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey(Place.id), nullable=False)
        user_id = Column(String(60), ForeignKey(User.id), nullable=False)
        user = relationship("User")

    else:
        place_id = ""
        user_id = ""
        text = ""
