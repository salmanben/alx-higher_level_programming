#!/usr/bin/python3
"""
This module defines 'Rectangle' class
that inherits from 'BaseGeometry' class.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    This class represents a rectangle and inherits
    from the 'BaseGeometry' class.
    """

    def __init__(self, width, height):
        """
        Initialize a new rectangle wit
        h the specified width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
        
    def area(self):
        """
        Returns the area of rectangle.
        """
        return self.__width * self.__height
    
    def __str__(self):
        """
        Returns representation of the oinstance.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
