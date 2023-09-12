#!/usr/bin/python3
"""A module defines func to read file."""


def read_file(filename=""):
    """Read file."""
    with open(filename, "r") as file:
        data = file.read()
        print(data)
