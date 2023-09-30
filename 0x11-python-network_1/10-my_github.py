#!/usr/bin/python3
"""Python script that takes your GitHub credentials"""
import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    url = "https://api.github.com/user"
    user_name = sys.argv[1]
    passwd = sys.argv[2]
    credentials = (user_name, passwd)
    res = requests.get(url, auth=credentials)
    print(res.json()['id'])
