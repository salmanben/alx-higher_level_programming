#!/usr/bin/python3
'''A module containing a class with restrictions.
'''


class LockedClass:
    '''Represents a class with restricted attribute modification.
    
    Attributes:
        __slots__ (list): A list containing the allowed attribute names.
    '''
    __slots__ = ['first_name']

