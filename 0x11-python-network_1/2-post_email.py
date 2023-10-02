#!/usr/bin/python3
"""a Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response """
import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    parameters = urllib.parse.urlencode({'email': email}).encode('utf-8')
    with urllib.request.urlopen(url=url, data=parameters) as response:
        print(response.read().decode('utf-8'))
