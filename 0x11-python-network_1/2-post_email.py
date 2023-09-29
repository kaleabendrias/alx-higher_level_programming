#!/usr/bin/env python3
# Write a Python script that takes in a URL and an email, sends a POST
import urllib.request
import sys

url = sys.argv[1]
email = sys.argv[2]
data = urllib.parse.urlencode(email)
data = data.encode('ascii')
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as res:
    body = res.read()
    print(body)
