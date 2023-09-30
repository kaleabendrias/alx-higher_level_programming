#!/usr/bin/python3
"""Python script that takes in a URL, sends a request"""
import requests
import sys

url = sys.argv[1]
res = requests.get(url).headers
print(res['X-Request-Id'])
