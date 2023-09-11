#!/usr/bin/python3
"""
This module defines 'Square' class that inherits from 'Rectangle' class.
"""


class Square(Rectangle):
    """
    This class represents a Square and inherits from the 'Rectangle' class.
    """

    def __init__(self, size):
        """
        Initialize a new square with the specified size.

        Args:
            size (int): The width of the rectangle.
        """
        self.integer_validator("size", size)
        self.__size = size
        
    def area(self):
        """
        Returns the area of square.
        """
        return self.__size * self.__size
    
    def __str__(self):
        """
        Returns representation of the instance.
        """
        return f"[Rectangle] {self.__size}/{self.__size}"
