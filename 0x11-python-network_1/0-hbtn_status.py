#!/usr/bin/python3
"""A python script fetches https://alx-intranet.hbtn.io/status"""
import urllib.request


with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
    content = response.read()
if __name__ == "__main__":
    print(f"Body response:\n\t" +
          f"- type: {type(content)}\n\t- content: {content}\n\t" +
          f"- utf8 content: {content.decode('utf-8')}")
