#!/usr/bin/python3
'''Defines  module for editing objects.
'''


def add_new_attribute(obj, attr_name, attr_value):
    '''Add a new attribute to an object if it is possible.
    '''
    if hasattr(obj, '__dict__'):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")
