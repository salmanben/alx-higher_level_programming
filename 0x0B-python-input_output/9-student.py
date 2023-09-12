#!/usr/bin/python3
"""A module defines 'Student' class"""


class Student:
    """Representation of 'Student' class"""
    
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def to_json(self):
        """Retrieves a dictionary representation of a Student instance"""
        dict_data = self.__dict__
        ser_data = {}
        for key, value in dict_data.items():
            if isinstance(value, (list, dict, str, int, bool)):
                ser_data[key] = value
        return ser_data
