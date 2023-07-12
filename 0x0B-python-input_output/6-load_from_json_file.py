#!/usr/bin/python3
"""Defines a JSON file-reading fxn."""
import json


def load_from_json_file(filename):
    """Reads an Json_string from a JSON file
      while converting to a Python object

    Args:
        filename (str): The path of the file.

    Returns:
        any: The read Python object
    """
    with open(filename) as f:
        return json.load(f)
