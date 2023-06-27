#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        ans = fct(*args)
    except Exception:
        ans = None
        print(f"Exception: {sys.exc_info()[1]}", file=sys.stderr)
    return ans
