#!/usr/bin/python3
"""The add_item Module"""


import json
import sys
import os


load_from = __import__('6-load_from_json_file').load_from_json_file
save_to = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"
args = [arg for arg in sys.argv[1:]]

if os.path.exists(filename) and os.stat(filename).st_size > 0:
    my_list = load_from(filename)
else:
    my_list = []

for arg in args:
    my_list.append(arg)
save_to(my_list, filename)
