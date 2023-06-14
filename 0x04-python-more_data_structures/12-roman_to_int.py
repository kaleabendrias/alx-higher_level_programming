#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return (0)
    roman_val = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
            }
    res = 0
    prev_val = 0

    for symbol in roman_string[::-1]:
        val = roman_val.get(symbol, 0)
        if (val >= prev_val):
            res += val
        else:
            res -= val
        pre_val = val

    return (res)
