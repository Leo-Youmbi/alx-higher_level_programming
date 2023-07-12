#!/usr/bin/python3
"""Defines a JSON file-writing fxn."""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object in JSON file

    Args:
        my_obj (_type_): The object to saved in the JSON file
        filename (str): The path of the file
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
