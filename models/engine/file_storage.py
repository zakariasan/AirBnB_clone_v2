#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}
    classes = {
                'BaseModel': BaseModel, 'User': User, 'Place': Place,
                'State': State, 'City': City, 'Amenity': Amenity,
                'Review': Review
                }

    def all(self, cls=None):
        """Returns a dictionary of __object__"""
        NewDict = {}

        if cls is None:
            return self.__objects
        else:
            if cls.__name__ in self.classes:
                for key, val in self.__objects.items():
                    if key.split('.')[0] == cls.__name__:
                        NewDict.update({key: val})

        return NewDict

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    value = eval(val["__class__"])(**val)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        Delete obj
        """
        if obj is None:
            return
        for key, value in FileStorage.__objects.items():
            if value == obj:
                del FileStorage.__objects[key]
                break

    def close(self):
        """ deserializing the JSON file to objects"""
        self.reload()
