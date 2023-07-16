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
            for keyed, valued in kwargs.items():
                if keyed == '__class__':
                    continue
                elif keyed == 'updated_at':
                    valued = datetime.strptime(valued, "%Y-%m-%dT%H:%M:%S.%f")
                elif keyed == 'created_at':
                    valued = datetime.strptime(valued, "%Y-%m-%dT%H:%M:%S.%f")
                if 'id' not in kwargs.keyed():
                    self.id = str(uuid4())
                if 'created_at' not in kwargs.keyed():
                    self.created_at = datetime.now()
                if 'updated_at' not in kwargs.keyed():
                    self.updated_at = datetime.now()
                setattr(self, keyed, valued)
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
