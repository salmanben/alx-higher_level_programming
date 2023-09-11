#!/usr/bin/python3

"""
This module defines a custom list class that extends the built-in list class.
"""


class MyList(list):
    """
    A custom list class that extends the built-in list class.
    """

    def print_sorted(self):
        """
        Print the elements of the list in sorted order.

        This method sorts the elements of the list and prints the sorted list.
        """
        sorted_list = sorted(self)
        print(sorted_list)
