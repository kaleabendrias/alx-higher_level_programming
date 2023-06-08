#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv) - 1
    total = 0
    for i in range(length):
        total += int(sys.argv[i + 1])
    print("{}".format(total))
