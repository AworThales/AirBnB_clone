#!/usr/bin/python3
""" The Class Place """

from models.base_model import BaseModel


class Place(BaseModel):
    """The Place class that inherits BaseModel """
    name = ""
    description = ""
    city_id = ""
    user_id = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
