#!/usr/bin/python3
"""Python script that takes in a URL and an email address"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    res = requests.post(url, data={'email': email})
    print(res.text)
