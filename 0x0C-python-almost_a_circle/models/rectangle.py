#!/usr/bin/python3
"""Defines 'Rectangle' class."""

from models.base import Base

class Rectangle(Base):
    """Represents the Rectangle class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the instance."""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Get width value."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set new value to width property."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get height value."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set new value to height property."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get x value."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set new value to x property."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get y value."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set new value to y property."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area value of the Rectangle instance."""
        return self.__width * self.__height

    def display(self):
        """Prints in stdout the Rectangle
        instance with the character '#'."""
        print("\n" * self.__y)
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """Defines the instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    
    def update(self, *args, **kwargs):
        """Assigns a key/value argument to attributes."""
        if args:
            attribute_names = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
               setattr(self, attribute_names[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
    
    def to_dictionary(self):
        """"Returns the dictionary representation of a Rectangle."""
        attribute_names = ['x', 'y', 'id', 'height', 'width']
        return {attr: getattr(self, attr) for attr in attribute_names}
