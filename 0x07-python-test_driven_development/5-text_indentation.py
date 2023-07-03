#!/usr/bin/python3
""" prints new line if it incounters ., ?, :."""


def text_indentation(text):
    """ prints newline after getting some chars"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    lines = text.splitlines()
    result = ""
    characters = [".", "?", ":"]
    for line in lines:
        stripped = line.rstrip()
        for char in stripped:
            result += char.strip()
            if char in characters:
                result += "\n\n"
    print(result.rstrip())
