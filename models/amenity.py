#!/usr/bin/python3
"""amenity.py module"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Inherits from the BaseModel class"""
    name = ""

    def __init__(self, **kwargs):
        """Initializes the instance of the class"""
        super().__init__(**kwargs)
