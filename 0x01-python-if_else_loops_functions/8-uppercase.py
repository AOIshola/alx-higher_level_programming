#!/usr/bin/python3
def uppercase(str):
    for c in range(len(str)):
        if ord(str[c]) >= 97 and ord(str[c]) < 123:
            offset = 32
        else:
            offset = 0
        print("{:c}".format(ord(str[c]) - offset), end="")
    print()
