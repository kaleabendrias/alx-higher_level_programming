#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if (type(value) == int):
            print(value)
            return (True)
        else:
            return (False)
    except:
        pass

