#!/usr/bin/python3
# Write a Python script that fetches https://alx-intranet.hbtn.io/status
import urllib.request

url = "https://alx-intranet.hbtn.io/status"
with urllib.request.urlopen(url) as res:
    html = res.read()
    print("Body response:$")
    print(f'\t - type: {type(res)}')
    print(f'\t - content: {html}')
    print(f"\t - utf8 content:", html.decode("utf-8"))
