#!/usr/bin/python3
"""
This module defines the 'Rectangle' class.
"""


class Rectangle:
    """
    A class representing a rectangle.

    Attributes:
        number_of_instances (int): A class-level counter tracking the number of instances created.
        print_symbol (can be any type): The symbol used for representing the rectangle in string form.

    Methods:
        __init__(self, width=0, height=0): Initialize a Rectangle object with a given width and height.
        width (property): Get or set the width of the rectangle.
        height (property): Get or set the height of the rectangle.
        area(self): Calculate and return the area of the rectangle.
        perimeter(self): Calculate and return the perimeter of the rectangle.
        __str__(self): Return a string representation of the rectangle using the specified symbol.
        __repr__(self): Return a string representation of the rectangle.
        __del__(self): Print a message when an instance is deleted.
        bigger_or_equal(rect_1, rect_2): returns the biggest rectangle based on the area.
    """
    number_of_instances = 0
    print_symbol = '#'
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        returns the biggest rectangle based on the area.

        Args:
            rect_1 (Rectangle)
            rect_2 (Rectangle)

        Raises:
            TypeError: If rect_1 or rect_2  are not instance of Rectangle class.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if  rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1
            
        
        
    def __init__(self, width=0, height=0):
        """
        Initialize a Rectangle object with a given width and height.

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is negative.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Get the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The new width value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The new height value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
        
    def area(self):
        """
        return the rectangle area.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle. If width or height is 0, returns 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
    
    def __str__(self):
        """
        Returns a string represents the rectangle using a symbol
        """
        my_rect = ""
        for i in range(self.__height):
            for j in range(self.__width):
                my_rect += self.print_symbol
            my_rect += '\n'
        return my_rect
    
    def __repr__(self) :
        """
        return a string representation of the rectangle
        """
        return f"Rectangle({self.__width},{self.__height})"
    
    def __del__(self):
        """
        prints message when an instance is deleted
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

my_rectangle_1 = Rectangle(8, 4)
my_rectangle_2 = Rectangle(2, 3)

if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
    print("my_rectangle_1 is bigger or equal to my_rectangle_2")
else:
    print("my_rectangle_2 is bigger than my_rectangle_1")


my_rectangle_2.width = 10
my_rectangle_2.height = 5
if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
    print("my_rectangle_1 is bigger or equal to my_rectangle_2")
else:
    print("my_rectangle_2 is bigger than my_rectangle_1")
