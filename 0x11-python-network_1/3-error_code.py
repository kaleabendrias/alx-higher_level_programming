#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as res:
            body = res.read()
            print(body.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
