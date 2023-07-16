#!/usr/bin/python3
""" This is the Class Review """
from models.base_model import BaseModel


class Review(BaseModel):
    """ This the Review class that inherits BaseModel """
    text = ""
    place_id = ""
    user_id = ""
