#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initialize a new Square

        Args:
            size (int): The size of a new square.
        """
        self.__size = size

    @property
    def size(self):
        """Returns the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2
