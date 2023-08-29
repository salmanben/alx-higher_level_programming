"""
This module defines 'Square' class.
"""


class Square:
    """
    A class representing a square.

    defines 'size' instance attribute.

    defines methods to get and set value to the attribute size.

    defines 'area' methods to calculate the area of square.
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
        if not isinstance(size, (int, float)):
            raise TypeError('size must be a number')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

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
            value (int or float): The new size of the square's sides.

        Raises:
            TypeError: If 'value' is not a number (integer or float).
            ValueError: If 'value' is negative.
        """
        if not isinstance(value, (int, float)):
            raise TypeError('size must be a number')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            The area of the square.
        """
        return self.__size * self.__size

    def __eq__(self, other):
        """
        Compare two Square instances based on their area.

        Returns:
            True if areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Compare two Square instances based on their area.

        Returns:
            True if areas are not equal, False otherwise.
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """
        Compare two Square instances based on their area.

        Returns:
            True if the area of the first square is greater than the area of the second square, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Compare two Square instances based on their area.

        Returns:
            True if the area of the first square is greater than or equal to the area of the second square, False otherwise.
        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """
        Compare two Square instances based on their area.

        Returns:
            True if the area of the first square is less than the area of the second square, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Compare two Square instances based on their area.

        Returns:
            True if the area of the first square is less than or equal to the area of the second square, False otherwise.
        """
        return self.area() <= other.area()
