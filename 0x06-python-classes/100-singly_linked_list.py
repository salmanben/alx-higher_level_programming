"""
This module defines the Node and SinglyLinkedList classes for a singly linked list.
"""

class Node:
    """
    A class representing a node of a singly linked list.
    
    Defines 'data' and 'next_node' instance attributes.
    """

    def __init__(self, data, next_node=None):
        """
        Initialize a new Node instance.
        
        Args:
            data: The data to be stored in the node.
            next_node: The next node in the linked list (default is None).
            
        Raises:
            TypeError: If 'data' is not an integer or if 'next_node' is not a Node object or None.
        """
        if not isinstance(data, int):
            raise TypeError('data must be an integer')
        self.__data = data

        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError('next_node must be a Node object')
        self.__next_node = next_node

    @property
    def data(self):
        """
        Retrieve the value of the private attribute 'data'.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Set a new value to the private attribute 'data'.

        Args:
            value: The new value for the node's data.

        Raises:
            TypeError: If 'value' is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """
        Retrieve the value of the private attribute 'next_node'.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set a new value to the private attribute 'next_node'.

        Args:
            value: The new value for the node's next_node.

        Raises:
            TypeError: If 'value' is not a Node object or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError('next_node must be a Node object')
        self.__next_node = value

class SinglyLinkedList:
    """
    A class representing a singly linked list.

    Defines 'head' instance attribute.
    """

    def __init__(self):
        """
        Initialize a new SinglyLinkedList instance with an empty head.
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Insert a new Node into the correct sorted position in the list (increasing order).
        
        Args:
            value: The value to be inserted into the linked list.
        """
        new_node = Node(value)
        
        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return
        
        current = self.__head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node
        
        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """
        Generate a string representation of the linked list.
        
        Returns:
            A string containing each node's data, one node per line.
        """
        result = []
        current = self.__head
        while current:
            result.append(str(current.data))
            current = current.next_node
        return '\n'.join(result)
