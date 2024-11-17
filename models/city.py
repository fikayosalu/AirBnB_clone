#!/usr/bin/python3
"""city.py module"""
from models.base_model import BaseModel


class City(BaseModel):
    """It inherits from the BaseModel class"""
    name = ""
    state_id = ""

    def __init__(self, **kwargs):
        """Initializes the instance of the class"""
        super().__init__(**kwargs)
