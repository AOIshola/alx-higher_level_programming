#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and displays the value
of the variable X-Request-Id in the response header requests package"""


import requests
import sys

req = requests.get(sys.argv[1])
print(req.headers["X-Request-Id"])
