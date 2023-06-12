#!/usr/bin/python3
def multiple_returns(sentence):
    new_t = ()
    if (len(sentence) == 0):
        new_t = 0, "None"
    else:
        new_t = len(sentence), sentence[0]
    return (new_t)
