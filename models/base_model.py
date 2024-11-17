#!/usr/bin/python3
"""base_model module"""
import uuid
from datetime import datetime
import json
import models


class BaseModel:
    """
    Defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes instances of the class with attributes
        id - A unique ID for each instance
        created_at - Time when an instance is created
        updated_at - Time whenever an object is modified
        kwargs represents a dictionary that its key/value pair is unpacked
        to initializes an instance with attributes
        """
        if len(kwargs) > 0:
            for attr, value in kwargs.items():
                if attr != "__class__":
                    if attr == 'created_at' or attr == 'updated_at':
                        setattr(self, attr, datetime.fromisoformat(value))
                    else:
                        setattr(self, attr, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ A string representation instances of the class"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the public instance attribute with the current time"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returs a dictionary containing all keys/values of __dict__
        of the instance
        __class__ key is be added to the dictionary with the class name
        of the object"""
        attributes = self.__dict__
        class_dict = {attr: value.isoformat() if attr ==
                      'created_at' or attr == 'updated_at' else value for attr,
                      value in attributes.items()}
        class_dict['__class__'] = self.__class__.__name__
        return class_dict
