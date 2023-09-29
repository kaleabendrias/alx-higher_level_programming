#!/usr/bin/python3
#  a Python script that takes in a URL, sends a request to the URL
import requests
import sys

url = sys.argv[1]
res = requests.get(url)
if (res.status_code >= 400):
    print(f"Error code: {res.status_code}")
else:
    print(res.text)
