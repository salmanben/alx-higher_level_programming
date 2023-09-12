#!/usr/bin/python3
"""A module defines func to write into file."""


def write_file(filename="", text=""):
    """Write into file.
    Return: The number of characters written.
    """
    with open(filename, "w") as file:
        num_bytes = file.write(text)
    return num_bytes
