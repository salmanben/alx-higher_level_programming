#!/usr/bin/python3

"""
This module defines 'Square' class.
"""


class Square:
    """
    A class representing a square.

    This class define the size  attribute of the instance.
    """
    def __init__(self, size):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square's sides (default is 0).
        """
        self.__size = size
