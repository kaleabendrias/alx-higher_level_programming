#!/usr/bin/python3
"""Python script that fetches a url"""
import requests

url = "https://alx-intranet.hbtn.io/status"
res = requests.get(url)
print("Body response:$")
print(f"\t- type: {type(res.text)}")
print(f"\t- content: {res.content.decode('utf-8')}")
