#!/usr/bin/python3
def safe_print_division(a, b):
    sum = None
    try:
        sum = a / b
    except:
        pass
    finally:
        print("Inside result: {}".format(sum))
        return (sum)
