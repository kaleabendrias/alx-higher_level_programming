#!/usr/bin/python3
# a Python script that takes in a URL and an email address
import requests
import sys

url = sys.argv[1]
email = sys.argv[2]
res = requests.get(url, data={'email': email})
print(res.text)
