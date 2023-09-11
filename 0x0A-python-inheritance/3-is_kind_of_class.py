#!/usr/bin/python3

"""
This module defines a function to check if an object is an instance of a specified class or a subclass of that class.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of a specified class or a subclass of that class.

    Parameters:
    obj (object): The object to be checked.
    a_class (class): The class to compare with.

    Returns:
    bool: True if the object is an instance of the specified class or a subclass; otherwise, False.
    """
    if isinstance(obj, a_class) or issubclass(type(obj), a_class):
        return True
    else:
        return False
