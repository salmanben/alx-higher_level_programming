#!/usr/bin/python3
"""
This module defines 'Rectangle' class
that inherits from 'BaseGeometry' class.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    This class represents a rectangle
    and inherits from the 'BaseGeometry' class.
    """

    def __init__(self, width, height):
        """
        Initialize a new rectangle with
        the specified width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        super().integer_validator("width", width)
        super().__width = width
        super().integer_validator("height", height)
        super().__height = height
