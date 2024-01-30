#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and displays the value
of the variable X-Request-Id in the response header requests package"""


import requests
import sys

if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    try:
        print(req.headers["X-Request-Id"])
    except KeyError as e:
        pass
