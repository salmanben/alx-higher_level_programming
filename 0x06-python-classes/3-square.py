#!/usr/bin/python3

"""
This module defines 'Square' class.
"""


class Square:
    """
    A class representing a square.

    defines 'size' instance attribute.

    define 'area' method to calc the area of square.
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

    def area(self):
        """
        Calculate and print the area of the square.

        The area is calculated as the square of the 'size' attribute.

        Returns:
            The area
        """
        return self.__size * self.__size
