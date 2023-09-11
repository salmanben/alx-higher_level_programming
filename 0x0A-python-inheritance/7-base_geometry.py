#!/usr/bin/python3

"""
This module defines 'BaseGeometry' class.
"""


class BaseGeometry:
    """
    This class defines a base geometry class with methods for area calculation and integer validation.
    """

    def area(self):
        """
        Calculate the area of the geometry.

        Raises:
            Exception: This exception is raised when this method is invoked.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate that a value is an integer and greater than or equal to 0.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value < 0:
            raise ValueError(f"{name} must be greater than or equal to 0")
