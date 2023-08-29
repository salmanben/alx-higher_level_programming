#!/usr/bin/python3
"""
This module defines 'Square' class.
"""


class Square:
    """
    A class representing a square.

    defines the 'size' and 'position' instance attributes.

    deifines methods to get and set value to the attributes(size, position).

    and methods to calc the area of square and drwaw the square by '#'.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square's sides (default is 0).
            position (tuple): contains two elements of type int

        Raises:
            TypeError: If 'size' is not an integer 
            or position is not a tuple of 2 positive integers.
            ValueError: If 'size' is negative.
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
        if not isinstance(position, tuple)
        or not isinstance(position[0], int)
        or not isinstance(position[1], int)
        or position[0] < 0 or position[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = position

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

    @property
    def position(self):
        """
        Retrieve the value of the private attribute 'position'.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set a new value to the private attribute 'position'.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If 'position' is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple)
        or not isinstance(value[0], int)
        or not isinstance(value[1], int)
        or value[0] < 0 or value[1] < 0:


           raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Print the square with the character '#' in stdout.

        If size is equal to 0, it prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
