#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first = sentence[0]
    if (length == 0):
        new_t = (0, "None")
    else:
        new_t = (length, first)
    return (new_t)
