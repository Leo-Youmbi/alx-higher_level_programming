#!/usr/bin/python3
"""Defines a text file-reading function."""


def read_file(filename=""):
    """Print the content of an encoded file.

    Args:
        filename (str, optional): Path of file to be read. Defaults to "".
    """
    with open(filename, mode='r', encoding='utf-8') as f:
        print(f.read(), end='')
