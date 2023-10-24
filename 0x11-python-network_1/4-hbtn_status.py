#!/usr/bin/python3
"""Python script that fetches a url"""
import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    res = requests.get(url)
    print("Body response:")
    print(f"\t- type: {type(res.text)}")
    print(f"\t- content: {res.content.decode('utf-8')}")
