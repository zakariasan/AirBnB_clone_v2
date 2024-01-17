#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import models
from models.city import City
import shlex


class State(BaseModel, Base):
    """ State class """
    if models.env_type == "db":
        __tablename__ = "states"
        name = Column(String(120), nullable=False)
        cities = relationship(
                "City",
                cascade='all, delete, delete-orphan',
                backref="state")
    else:
        name = ''

    if models.env_type != "db":
        @property
        def cities(self):
            """for FileStorage: getter attribute cities"""
            var = models.storage.all()
            CityList = []
            result = []
            for key in var:
                city = key.replace('.', ' ')
                city = shlex.split(city)
                if (city[0] == 'City'):
                    CityList.append(var[key])
            for elem in CityList:
                if (elem.state_id == self.id):
                    result.append(elem)
            return (result)

    def __init__(self, *args, **kwargs):
        """State inherits from BaseModel and Base"""
        super().__init__(*args, **kwargs)
