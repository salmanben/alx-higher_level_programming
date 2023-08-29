#!/usr/bin/python3
"""
This module defines 'Square' class.
"""


class Square:
    """
    A class representing a square.

    defines 'size' instance attribute.

    deifines methods to get and set value to the attribute size.

    defines 'area' methods to calc the area of square.
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

    @property
    def size(self):
        """
        Retrieve the value of the private attribute 'size'.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set a new value to the private attribute 'size'.

        Args:
            value (int): The new size of the square's sides.

        Raises:
            TypeError: If 'value' is not an integer.
            ValueError: If 'value' is negative.
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
