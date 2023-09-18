#!/usr/bin/python3
"""Defines 'Square' class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents the Square class."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the instance."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Defines the instance."""
        return (
            f"[{self.__class__.__name__}] ({self.id}) "
            f"{self.x}/{self.y} - {self.width}"
               )

    @property
    def size(self):
        """Get size value."""
        return self.width

    @size.setter
    def size(self, value):
        """Set new value to size attribute."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns a key/value argument to attributes."""
        if args:
            attribute_names = ['id', 'width', 'height', 'x', 'y']
            if len(args) > 1:
                args = list(args)
                args.insert(1, args[1])
            for i in range(len(args)):
                setattr(self, attribute_names[i], args[i])
        else:
            if 'size' in kwargs:
                kwargs['width'] = kwargs['size']
                kwargs['height'] = kwargs['size']
                del kwargs['size']
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """"Returns the dictionary representation of a Square."""
        return {'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y}
