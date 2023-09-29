#!/usr/bin/python3
# a Python script that fetches a url
import requests

url = "https://alx-intranet.hbtn.io/status"
req = requests.get(url)
print("Body response:$")
print(f"\t- type: {type(req)}")
print(f"\t- content: {req.content.decode('utf-8')}")
