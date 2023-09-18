#!/usr/bin/python3
"""Defines 'Base' class."""

import json

class Base:
    """Represents the Base class of all other
    classes in this project."""
    __nb_objects = 0
    
    def __init__(self, id=None):
        """Initialize the instance."""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
   
    @staticmethod
    def to_json_string(list_dictionaries):
       """Returns the JSON string representation
       of 'list_dictionaries.'"""
       if list_dictionaries:
           return json.dumps(list_dictionaries)
       return []

    @classmethod
    def save_to_file(cls, list_objs):
        """rites the JSON string representation
        of 'list_objs' to a file.
        
        list_object: is a list of instances who inherits of Base.
        """
        filename = f"{cls.__name__}.json"
        if  not list_objs:
            list_dict = []
        else:
            list_dict = [obj.to_dictionary() for obj in list_objs]
            with open(filename, 'w') as file:
                file.write(cls.to_json_string(list_dict))
                
    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string
        representation 'json_string'."""
        if json_string:
           return json.loads(json_string)
        return []
    
    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set."""
        new_inst = cls(1, 1, 1, 1)
        new_inst.update(**dictionary)
        return new_inst
    
    @classmethod
    def load_from_file(cls):
        """Returns a list of instances."""
        filename = f"{cls.__name__}.json"
        list_dict = []
        with open(filename, 'r') as file:
            list_dict = file.read()
        list_dict = cls.from_json_string(list_dict)
        if not list_dict:
            return []
        list_inst = [cls.create(**item) for item in list_dict]
        return list_inst

