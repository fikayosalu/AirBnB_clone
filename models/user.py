#!/usr/bin/python3
"""user module"""
from models.base_model import BaseModel


class User(BaseModel):
    """A user class that inherits from the BaseModel class"""
    def __init__(self):
        """Initializes the objects of the user class with these attributes"""
        super().__init__()
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
