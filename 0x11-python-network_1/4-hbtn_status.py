#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status using requests package"""


import requests

if __name__ == "__main__":
    req = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:\n\t- type: {}\n\t- content: {}".format(
        type(req.text), req.text))
