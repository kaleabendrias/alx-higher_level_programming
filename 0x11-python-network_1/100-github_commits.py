#!/usr/bin/python3
"""Python script that takes 2 arguments"""
import requests
import sys

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    res = requests.get(url).json()
    try:
        for i in range(10):
            print(f"{res[i]['sha']}: {res[i]['commit']['author']['name']}")
    except IndexError:
        pass
