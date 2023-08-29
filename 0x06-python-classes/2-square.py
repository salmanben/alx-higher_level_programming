#!/usr/bin/python3

"""
This module defines 'Square' class.
"""


class Square:
    """
    A class representing a square.

    This class defines the size  attribute of the instance.
    """
    def __init__(self, size=0):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square's sides (default is 0).

        Raises:
            TypeError: If 'size' is not an integer.
            ValueError: If 'size' is negative.
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
