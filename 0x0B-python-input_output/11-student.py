#!/usr/bin/python3
"""A module defines 'Student' class"""


class Student:
    """Representation of 'Student' class"""
    
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance"""
        if (type(attrs) == list and
                all(type(item) == str for item in attrs)):
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}
        return self.__dict__
    
    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance."""
        self.__dict__.clear()
        for k, v, in json.items():
            setattr(self, k, v)
