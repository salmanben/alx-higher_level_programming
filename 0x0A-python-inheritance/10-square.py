#!/usr/bin/python3
"""
This module defines 'Square' class
that inherits from 'Rectangle' class.
"""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """
    This class represents a Square
    and inherits from the 'Rectangle' class.
    """
    def __init__(self, size):
        """
        Initialize a new square with the specified size.
        Args:
            size (int): The width of the rectangle.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
