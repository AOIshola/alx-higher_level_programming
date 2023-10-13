#!/usr/bin/python3

def roman_to_int(roman_string):
    syms = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if not isinstance(roman_string, str) or not roman_string:
        return (0)
    result = 0
    prev = 0
    for symbol in roman_string:
        if symbol in syms:
            if prev < syms[symbol]:
                result += (syms[symbol] - (2 * prev))
                prev = syms[symbol]
            else:
                prev = syms[symbol]
                result += syms[symbol]
    return (result)
