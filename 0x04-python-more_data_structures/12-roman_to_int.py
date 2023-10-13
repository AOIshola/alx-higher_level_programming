#!/usr/bin/python3

def roman_to_int(roman_string):
    symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
            'D': 500, 'M': 1000}
    if not isinstance(roman_string, str) or not roman_string:
        return (0)
    result = 0
    prev = 0
    for symbol in roman_string:
        if symbol in symbols:
            if prev < symbols[symbol]:
                result += (symbols[symbol] - (2 * prev))
                prev = symbols[symbol]
            else:
                prev = symbols[symbol]
                result += symbols[symbol]
    return (result)
