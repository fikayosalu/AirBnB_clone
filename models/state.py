#!/usr/bin/python3
"""state.py module"""
from models.base_model import BaseModel


class State(BaseModel):
    """Inherits from the BaseModel class"""
    name = ""

    def __init__(self, **kwargs):
        """Initializes the instance of the class"""
        super().__init__(**kwargs)
