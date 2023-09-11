#!/usr/bin/python3
'''Module defines ' BaseGeometry' class.
'''


class BaseGeometry:
    '''This class used as parent  for all geomatry classes.
    '''

    def area(self):
        '''raise Exeception when method
        is invoked
        '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''check if a value is an integer
        '''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
