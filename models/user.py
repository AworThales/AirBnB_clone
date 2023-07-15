#!/usr/bin/python3
""" User Class """
from models.base_model import BaseModel


class User(BaseModel):
    """ This is the User class that inherits BaseModel """
    email = ""
    first_name = ""
    last_name = ""
    password = ""
