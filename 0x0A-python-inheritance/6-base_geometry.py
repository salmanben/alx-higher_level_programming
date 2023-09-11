#!/usr/bin/python3

"""
This module defines 'BaseGeometry' class.
"""


class BaseGeometry:
    """
    This class defines an instance method:
    def area(self):that raises an Exception
    with the message area() is not implemented
    """
    def area(self):
        """
        Raises:
            Exception: This exception is raised
            when this method is invoked.
        """
        raise Exception("area() is not implemented")
