#!/usr/bin/python3
"""Define a Single Linked List"""


class Node:
    """Represent a node."""
    def __init__(self, data, next_node=None):
        """Initialize a new Node

        Args:
            data (int): value of current node
            next_node (Node, optional): Pointer to next node. Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get/set the data of the Node."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get/set the next_node of the Node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a single linked list of nodes"""
    def __init__(self):
        """Initialize a new SinglyLinkedList"""
        self.__head = None

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        values = []
        curNode = self.__head
        while curNode is not None:
            values.append(str(curNode.data))
            curNode = curNode.next_node
        return ('\n'.join(values))

    def sorted_insert(self, value):
        """Insert a value in a sorted way

        Args:
            value (int): value to be inserted
        """
        if self.__head is None:
            self.__head = Node(value)
        else:
            newNode = Node(value)
            if self.__head.data > value:
                newNode.next_node = self.__head
                self.__head = newNode
            else:
                curNode = self.__head
                while (curNode.next_node is not None and
                       curNode.next_node.data < value):
                    curNode = curNode.next_node
                newNode.next_node = curNode.next_node
                curNode.next_node = newNode
