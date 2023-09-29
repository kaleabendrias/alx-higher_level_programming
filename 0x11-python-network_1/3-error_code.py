#!/usr/bin/python3
# a Python script that takes in a URL, sends a request to the URL
import urllib.request
import sys

url = sys.argv[1]
with urllib.request.urlopen(url) as res:
    body = res.read()
    if body:
        print(body.decode('utf-8'))
    else:
        print(f"Error code: {res.status}")
