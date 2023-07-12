#!/usr/bin/python3
"""Defines a function that deserializes a Json string"""
import json


def from_json_string(my_str):
    """Changes a json to Python object

    Args:
        my_str (any): The Json string to be deserialized.

    Returns:
        str: A deserialized string
    """
    return json.loads(my_str)
