#!/usr/bin/python3
'''
    Define the class Place.
'''
from models.base_model import BaseModel
import sqlalchemy
from sqlalchemy import Column, String, Integer, Float

class Place(BaseModel):
    '''
        Define the class Place that inherits from BaseModel.
    '''

    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey(City.id), nullable=False)
    user_id = Column(String(60), ForeignKey(User.id), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=False, default=0.0)
    longitude = Column(Float, nullable=False, default=0.0)
    amenity_ids = []
