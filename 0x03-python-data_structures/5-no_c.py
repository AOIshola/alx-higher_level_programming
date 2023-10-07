#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for char in range(len(my_string)):
        if my_string[char] not in "cC":
            new_str += my_string[char]
    return (new_str)
