#!/usr/bin/python3
def uppercase(str):
    for i in str:
        ascii = ord(i)
        if (97 <= ascii <= 122):
            upper_ascii = ascii - 32
            print('{}'.format(chr(upper_ascii)), end="")
        else:
            print('{}'.format(i), end="")
    print()
