#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
import shlex


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(120), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        CityDict = models.storage.all()
        CityList = []
        result = []
        for key in CityDict:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                CityList.append(CityDict[key])
        for elem in CityList:
            if (elem.state_id == self.id):
                result.append(elem)
        return (result)
