#!/usr/bin/python3
"""A module defines func to read file."""


def read_file(filename=""):
    """Read file."""
    with open(filename, encoding="utf-8")as file:
        print(file.read(), end="")
