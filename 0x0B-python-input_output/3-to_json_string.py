#!/usr/bin/python3
"""Defines a function that serializes an object"""
import json


def to_json_string(my_obj):
    """Changes a str to json

    Args:
        my_obj (any): The object to be serialized.

    Returns:
        str: The json string
    """
    return json.dumps(my_obj)
