#!/usr/bin/python3

"""
This module provides a function to retrieve a list of available attributes and methods of an object.
"""


def lookup(obj):
    """
    Return a list of available attributes and methods of an object.

    Parameters:
    obj (object): The object for which you want to retrieve attributes and methods.

    Returns:
    list: A list of strings containing the names of attributes and methods.
    """
    return dir(obj)
