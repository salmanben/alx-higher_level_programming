#!/usr/bin/python3
"""Module for converting objects to JSON-serializable dictionaries."""


def class_to_json(obj):
    """
    Convert an object to a JSON-serializable dictionary.

    Args:
        obj: An instance of a class with serializable attributes.

    Returns:
        dict: A dictionary representation of the object for JSON serialization.
    """
    serialized_obj = {}
    attributes = obj.__dict__
    for key, value in attributes.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serialized_obj[key] = value
    return serialized_obj
