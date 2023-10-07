#!/usr/bin/python3
def multiple_returns(sentence):
    str_len = len(sentence)
    if str_len == 0:
        first = None
    else:
        first = sentence[0]

    len_n_first = (str_len, first)
    return (len_n_first)
