#!/usr/bin/python3
"""A module defines func that 
appends text to file."""


def append_write(filename="", text=""):
    """Append to file.
    Return: The number of characters added.
    """
    with open(filename, "a") as file:
        num_bytes = file.write(text)
    return num_bytes
