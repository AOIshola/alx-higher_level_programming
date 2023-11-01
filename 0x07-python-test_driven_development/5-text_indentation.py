#!/usr/bin/python3
"""The Text Indentation Module"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after certain
    characters

    Parameters:
        text (str): text provided
    Returns: Nothing.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    char_delim = ['.', '?', ':']

    flag = False
    for idx in range(len(text)):
        if flag:
            if text[idx] != " ":
                print("{}".format(text[idx]), end="")
            elif text[idx] == " " and idx == len(text) - 1:
                pass
            else:
                idx += 1
            flag = False
        else:
            print("{}".format(text[idx]), end="")
        if text[idx] in char_delim:
            flag = True
            print("\n")
