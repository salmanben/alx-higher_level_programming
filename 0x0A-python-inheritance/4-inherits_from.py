#!/usr/bin/python3
"""
This module provides a function to check if an object  is an instance of a class
that inherited (directly or indirectly) from the specified class 
"""


def inherits_from(obj, a_class):
    """
    Check if an object  is an instance of a class
    that inherited (directly or indirectly) from the specified class 

    Parameters:
    obj (object): The object to be checked.
    a_class (class): The class to compare with.

    Returns:
    bool: True  if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class; otherwise, False.
    """
    return issubclass(type(obj), a_class)
