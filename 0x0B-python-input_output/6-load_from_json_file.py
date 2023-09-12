#!/usr/bin/python3
"""A module defines func that
creates an Object from a “JSON file”."""
import json


def load_from_json_file(filename):
    """Creates an Object from a “JSON file”.
    Return: The created object.
    """
    with open(filename, "r") as file:
        obj = json.load(file)
    return obj
