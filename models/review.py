#!/usr/bin/python3
"""review.py module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """The State class inherits from the BaseModel class"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, **kwargs):
        """Initializes instance of the class with attributes"""
        super().__init__(**kwargs)
