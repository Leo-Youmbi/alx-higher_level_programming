#!/usr/bin/python3
"""Defines an object attribute lookup function."""


def lookup(obj):
    """Return a list of an object's available attributes.

    Args:
        obj (Any): Object

    Returns:
        list: Object's attributes and members
    """
    return (dir(obj))
