#!/usr/bin/python3
# Python script that takes in a URL, sends a request to the URL
import urllib.request
import sys

url = sys.argv[1]
with urllib.request.urlopen(url) as res:
    body = res.headers()
    print(body['X-Request-Id'])
