#!/usr/bin/python3
"""Define Basemodel module."""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """This is the BaseModel class for AirRBnB clone project."""
    def __init__(self, *args, **kwargs):
        """Initialize the new BaseModel instance.
        Args:
            *args: not used.
             **kwargs: for key/value pairs of arguments.
             """
        if len(kwargs):
            time_format = "%Y-%m-%dT%H:%M:%S.%f"
            del kwargs["__class__"]
            for key, val in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(val, time_format)
                else:
                    self.__dict__[key] = val
        else:
            self.id = str(uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            models.storage.new(self)

    def __str__(self):
        """Prints string representation of object's
        class name, id and dictionary.
        """
        print("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """Update the update_at with the current time."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Returns the BaseModel instance's dictionary
        including __class__ as a key and class name as value.
        """
        obj_dict = self.__dict__.copy()
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        obj_dict["__class__"] = self.__class__.__name__
        return obj_dict

