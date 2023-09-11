#!/usr/bin/python3
"""
This module defines a function to check
if an object is an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Check if an object is an instance of a specified class.
    returns True if the object is an instance of the specified class,
    otherwise, False.
    """
    return (type(obj) is a_class)
