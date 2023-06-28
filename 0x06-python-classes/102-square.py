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

    def __eq__(self, other):
        """
        Compares two squares for equality based on their areas.

        Args:
            other (Square): The other square to compare.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Compares two squares for inequality based on their areas.

        Args:
            other (Square): The other square to compare.
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """
        Compares two squares for greater than based on their areas.

        Args:
            other (Square): The other square to compare.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Compares two squares for greater than or equal to based on their areas.

        Args:
            other (Square): The other square to compare.
        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """
        Compares two squares for less than based on their areas.

        Args:
            other (Square): The other square to compare.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Compares two squares for less than or equal to based on their areas.

        Args:
            other (Square): The other square to compare.
        """
        return self.area() <= other.area()
