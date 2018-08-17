#!/usr/bin/python3
'''
DBStorage schema using SQLAlchemy and MySQL
'''
import sqlalchemy
from sqlalchemy import create_engine
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import models


class DBStorage:
    '''
    Main database storage class
    '''

    __engine = None
    __session = None

    def __init__(self):
        '''
            Instantiation of a database storage class
        '''
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')
        my_sql = "mysql+mysqldb://{}:{}@{}/{}".format(user,
                                                      password,
                                                      host,
                                                      database)
        self.__engine = create_engine('{}'.format(my_sql),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        '''
            Queries database for specified classes

            Parameters:
                cls (object): the class to query

            Return:
                a dictionary of objects of the corresponding cls
        '''
        to_query = []
        new_dict = {}
        if cls is not None:
            results = self.__session.query(eval(cls)).all()
            for row in results:
                key = row.__class__.__name__ + '.' + row.id
                new_dict[key] = row
        else:
            for key, value in models.classes.items():
                try:
                    self.__session.query(models.classes[key]).all()
                    to_query.append(models.classes[key])
                except:
                    continue
            for classes in to_query:
                    results = self.__session.query(classes).all()
                    for row in results:
                        key = row.__class__.__name__ + '.' + row.id
                        new_dict[key] = row
        return new_dict

    def new(self, obj):
        '''
            Saves an object to the current session object

            Parameters:
                obj (object): the object to save in the session
        '''
        self.__session.add(obj)

    def save(self):
        '''
            Saves all changes to current session to the database
        '''
        self.__session.commit()

    def delete(self, obj=None):
        '''
            Deletes a specified object from the database

            Parameters:
                obj (object): the object to delete
        '''
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        '''
            Restarts the database engine session
        '''
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        '''
            Rempving session
        '''
        self.__session.close()
