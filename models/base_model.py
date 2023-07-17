#!/usr/bin/python3
""" Class BaseModel """
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """ The construct
    
     Methods:
        __init__(self, *args, **kwargs)
        __str__(self)
        __save(self)
        __repr__(self)
        to_dict(self)
        
    """

    def __init__(self, *args, **kwargs):
        """ Starting Construct """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == 'created_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if 'id' not in kwargs.key():
                    self.id = str(uuid4())
                if 'created_at' not in kwargs.key():
                    self.created_at = datetime.now()
                if 'updated_at' not in kwargs.key():
                    self.updated_at = datetime.now()
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """ String """
        return('[' + type(self).__name__ + '] (' + str(self.id) +
               ') ' + str(self.__dict__))

    def save(self):
        """ save function """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Return a dictonary """
        tha_dic = self.__dict__.copy()
        tha_dic['__class__'] = self.__class__.__name__
        tha_dic['created_at'] = self.created_at.isoformat()
        tha_dic['updated_at'] = self.updated_at.isoformat()
        return tha_dic
