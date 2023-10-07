#!/usr/bin/python3

def max_integer(my_list=[]):
    max_int = my_list[0]
    if len(my_list) == 0:
        return (None)
    for num in my_list:
        if num > max_int:
            max_int = num
    return (max_int)
