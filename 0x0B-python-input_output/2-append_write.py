#!/usr/bin/python3
"""appends a string at the end of text file"""


def append_write(filename="", text=""):
    with open(filename, 'a') as f:
        num = f.write(text)
    return num
            