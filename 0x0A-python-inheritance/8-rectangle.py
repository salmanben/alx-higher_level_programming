#!/usr/bin/python3
"""
This module defines 'Rectangle' class that inherits from 'BaseGeometry' class.
"""


class Rectangle(BaseGeometry):
    """
    This class represents a rectangle and inherits from the 'BaseGeometry' class.
    """

    def __init__(self, width, height):
        """
        Initialize a new rectangle with the specified width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
