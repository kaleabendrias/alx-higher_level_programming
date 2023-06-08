#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import *
    import sys

    argv = sys.argv[1:]
    argv_len = len(argv)
    operators = ["+", "-", "*", "/"]
    if argv_len != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif sys.argv[2] not in operators:
        print("Unknown operator. Available operators: +, -, *, /")
        exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if (sys.argv[2] == "+"):
            print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
        elif (sys.argv[2] == "-"):
            print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
        elif (sys.argv[2] == "*"):
            print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
        elif (sys.argv[2] == "/"):
            print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))

