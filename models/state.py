#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from os import environ


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(120), nullable=False)
    if environ['HBNB_TYPE_STORAGE'] == 'db':
        cities = relationship('City', cascade='all, delete', backref='state')

    @property
    def cities(self):
        from models import storage
        from models.city import City
        CityDict = models.storage.all()
        CityList = []
        for city in CityDict.values():
            if city.state_id == self.id:
                CityList.append(city)

        return CityList
