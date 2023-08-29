"""
This module defines 'Square' class.
"""


class Square:
    """
    A class representing a square.
    
    Defines the 'size' and 'position' instance attributes.
    Defines methods to get and set values for the attributes (size, position).
    Also defines methods to calculate the area of the square and draw the square using '#'.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square instance.
        
        Args:
            size (int): The size of the square's sides (default is 0).
            position (tuple): Contains two elements of type int
            
        Raises:
            TypeError: If 'size' is not an integer or if 'position' is not a tuple of 2 positive integers.
            ValueError: If 'size' is negative.
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
        
        if not isinstance(position, tuple) or not isinstance(position[0], int) or not isinstance(position[1], int) or position[0] < 0 or position[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = position
        
    def __str__(self):
        return self.my_print()

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
        if not isinstance(value, tuple) or not isinstance(value[0], int) or not isinstance(value[1], int) or value[0] < 0 or value[1] < 0:
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
        Generate a string representation of the square.

        If size is equal to 0, it generates an empty string.
        """
        square_str = ""
        if self.__size == 0:
            square_str += "\n"
        else:
            for i in range(self.__position[1]):
                square_str += "\n"
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    square_str += " "
                for j in range(self.__size):
                    square_str += "#"
                square_str += "\n"
        return square_str
