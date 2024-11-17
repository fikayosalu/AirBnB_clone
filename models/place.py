#!/usr/bin/python3
"""place.py module"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Inherits from the BaseModel class"""
    name = ""
    user_id = ""
    city_id = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, **kwargs):
        """Initializes the instance of the class"""
        super().__init__(**kwargs)
