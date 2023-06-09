#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)
    if (len(my_list) == 0):
        return (None)
    for i in range(length - 1):
        for j in range(0, length - i -1):
            if (my_list[j] > my_list[j + 1]):
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    return (my_list[-1])

