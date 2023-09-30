#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST"""
import requests
import sys

url = "http://0.0.0.0:5000/search_user"
if len(sys.argv) == 2:
    letter = sys.argv[1]
else:
    letter = ''
res = requests.post(url, data={'q': letter})
try:
    json_res = res.json()
    if json_res:
        print(f"[{json_res['id']} {json_res['name']}]")
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")
