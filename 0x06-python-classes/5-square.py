#!/usr/bin/python3

"""
This module defines 'Square' class.
"""


class Square:
    """
    A class representing a square.

    defines the 'size' instance attribute.

    deifines methods to get and set value to the attribute size.

    define methods to calc the area of square and drwaw the square by '#'.
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
        self.__size = size
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

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

    def area(self):
        """
        Calculate and print the area of the square.

        The area is calculated as the square of the 'size' attribute.

        Returns:
            The area
        """
        return self.__size * self.__size

    def my_print(self):
        """
        prints in stdout the square with the character #:
        if size is equal to 0, it pint an empty line
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end='')
                print()
