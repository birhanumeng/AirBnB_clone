#!/usr/bin/python3
"""Define the FileStorage module."""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Define class for FileStorage.
    Attributes:
        __file_path (str): path to the file.
        __objects (dict): instance's dictionary.
        """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets obj with key <obj class name>.id in __objects"""
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        tmp_dict = FileStorage.__objects
        obj_dict = {obj: tmp_dict[obj].to_dict() for obj in tmp_dict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        my_dict = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
            }
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r") as file_path:
            objects = json.load(file_path)
            FileStorage.__objects = {}
            for key in objects:
                name = key.split(".")[0]
                FileStorage.__objects[key] = my_dict[name](**objects[key])

