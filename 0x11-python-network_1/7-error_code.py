#!/usr/bin/python3
"""a Python script that takes in a URL, sends a request to the URL
and displays the body of the response."""
import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    req = requests.get(url)
    try:
        req.raise_for_status()
        print(req.text)
    except Exception:
        print(f"Error code: {req.status_code}")
